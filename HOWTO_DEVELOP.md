## Install package manager

### pnpm

Using corepack:

```shell
corepack prepare pnpm@latest --activate
```

or using `npm`:

```shell
npm install -g pnpm@latest
```

Verify the latest version.

```shell
pnpm --version
```

### Install dependencies

In order to develop plonetheme.barceloneta you need to execute on the root of the package::

```shell
pnpm install
```

You can also updated dependencies with

```shell
pnpm update
```

After executing this you can run the following command to watch for any scss changes
in the path `plonetheme.barceloneta/scss`::

```shell
pnpm watch
```

This will make sure that the many .scss files are compiled to .css on the fly
and then copied over to the theme.

If you simply want to compile all resources before a release run::

```shell
pnpm build
```


## Release Instructions

```{note}
You need the correct access rights to publish to npm or pypi.
```

- First create a pypi release using zest.releaser. This tool also creates the correct tag based on the setup.py version.
- After the pypi release edit the release version in package.json.
  Or better yet, run something like `pnpm version 3.2.0-alpha.5`
- Run: `pnpm publish`


### Pre-Releases

Based on https://survivejs.com/maintenance/packaging/publishing/#publishing-a-pre-release-version

- Change version in package.json to corresponding version in setup.py
- You can also use `pnpm version 3.0.0-beta1` - This will change the version in package.json and create a git tag.
- `pnpm publish --tag beta` - Publish the package under beta tag.
- Mark beta release as latest with `npm dist-tag add @plone/plonetheme-barceloneta-base@3.0.0-beta1 latest``

To consume the test version, users have to use `pnpm install @plone/plonetheme-barceloneta-base@beta`.


## Theme

See `plonetheme.barceloneta/plonetheme/barceloneta/theme/rules.xml` for the relevant Diazo theme rules.


## Fonts

Read `plonetheme.barceloneta/plonetheme/barceloneta/theme/roboto/README.rst` if you need to update the shipped fonts.
