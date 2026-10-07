from diazo.compiler import compile_theme
from lxml import etree
from lxml import html
from pathlib import Path

import unittest


class TestHeadResources(unittest.TestCase):
    def setUp(self):
        rules = Path(__file__).resolve().parents[1] / "theme" / "rules.xml"
        self.transform = etree.XSLT(
            compile_theme(str(rules), xsl_params={"ajax_load": False})
        )

    def render(self, head, body=None, **params):
        if body is None:
            body = '<div id="visual-portal-wrapper"><div id="portal-top"></div></div>'
        source = html.document_fromstring(
            f"<html><head>{head}</head><body>{body}</body></html>"
        )
        result = self.transform(source, **params)
        return source, html.document_fromstring(str(result))

    def test_head_resources_keep_source_order(self):
        source, result = self.render("""
            <title>Resource order</title>
            <meta id="charset" charset="utf-8">
            <script id="classic-before" src="before.js"></script>
            <link id="css-before" rel="stylesheet" href="before.css">
            <script id="import-map" type="importmap" nonce="test-nonce">
              {"imports": {"example": "/example.js"}}
            </script>
            <link id="module-preload" rel="modulepreload" href="/example.js"
                  crossorigin="anonymous" integrity="sha384-example">
            <style id="inline-css" media="screen">body { color: black; }</style>
            <script id="module" type="module">import "example";</script>
            <meta id="description" name="description" content="Example">
            <link id="css-after" rel="stylesheet" href="after.css" media="print">
            <script id="classic-after" src="after.js" defer="defer"></script>
            """)
        # Select in document order, not separately by tag: Firefox rejects an
        # import map if a module load or module preload has already started.
        self.assertEqual(
            result.xpath("/html/head/*[@id]/@id"),
            source.xpath("/html/head/*[@id]/@id"),
        )

    def test_resource_attributes_and_contents_are_preserved(self):
        source, result = self.render("""
            <script id="map" type="importmap" nonce="test-nonce">
              {"imports": {"example": "/example.js"}}
            </script>
            <link id="preload" rel="modulepreload" href="/example.js"
                  crossorigin="anonymous" integrity="sha384-example">
            <style id="style" media="screen" nonce="test-nonce">a > b {}</style>
            <script id="module" type="module" async="async"
                    crossorigin="use-credentials">import "example";</script>
            """)
        for original in source.xpath("/html/head/*[@id]"):
            with self.subTest(element=original.get("id")):
                copied = result.xpath(f'//*[@id="{original.get("id")}"]')
                self.assertEqual(len(copied), 1)
                self.assertEqual(copied[0].attrib, original.attrib)
                self.assertEqual(copied[0].text, original.text)

    def test_title_base_metadata_and_icons(self):
        _, result = self.render("""
            <title>Content title</title>
            <base href="https://example.org/site/" target="_self">
            <meta name="description" content="Content description">
            <link rel="apple-touch-icon" href="content-apple.png">
            <link rel="icon" href="favicon.ico" sizes="32x32">
            <link rel="apple-touch-icon-precomposed" href="precomposed.png">
            """)
        self.assertEqual(result.xpath("/html/head/title/text()"), ["Content title"])
        self.assertEqual(
            result.xpath("/html/head/base/@href"), ["https://example.org/site/"]
        )
        self.assertEqual(result.xpath("/html/head/base/@target"), ["_self"])
        self.assertEqual(
            result.xpath("/html/head/title/preceding-sibling::*[1]")[0].tag, "base"
        )
        self.assertEqual(
            result.xpath('/html/head/meta[@name="description"]/@content'),
            ["Content description"],
        )
        self.assertEqual(
            result.xpath('/html/head/link[@rel="apple-touch-icon"]/@href'),
            ["++theme++barceloneta/barceloneta-apple-touch-icon.png"],
        )
        self.assertEqual(
            result.xpath('/html/head/link[@rel="icon"]/@href'), ["favicon.ico"]
        )
        self.assertIn(
            "precomposed.png",
            result.xpath('/html/head/link[@rel="apple-touch-icon-precomposed"]/@href'),
        )

    def test_classic_resources_also_keep_source_order(self):
        source, result = self.render("""
            <script id="before" src="before.js"></script>
            <style id="inline">body { color: black; }</style>
            <link id="stylesheet" rel="stylesheet" href="site.css">
            <script id="after" src="after.js"></script>
            """)
        self.assertEqual(
            result.xpath("/html/head/*[@id]/@id"),
            source.xpath("/html/head/*[@id]/@id"),
        )

    def test_notheme_conditions(self):
        for body, params in (
            ("<main>Outside Plone</main>", {}),
            (
                '<div id="visual-portal-wrapper" class="template-manage-viewlets">'
                '<div id="portal-top"></div></div>',
                {},
            ),
            (
                '<div id="visual-portal-wrapper"><div id="portal-top"></div></div>',
                {"ajax_load": "true()"},
            ),
        ):
            with self.subTest(body=body, params=params):
                source, result = self.render(
                    '<title>Unthemed</title><script id="map" type="importmap">{}</script>'
                    '<link id="preload" rel="modulepreload" href="module.js">',
                    body=body,
                    **params,
                )
                # libxslt's HTML serializer adds a Content-Type meta tag.
                for meta in result.xpath('/html/head/meta[@http-equiv="Content-Type"]'):
                    meta.getparent().remove(meta)
                self.assertEqual(
                    [
                        (node.tag, node.attrib, node.text)
                        for node in result.find("head")
                    ],
                    [
                        (node.tag, node.attrib, node.text)
                        for node in source.find("head")
                    ],
                )
