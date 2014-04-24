module.exports = function (grunt) {
    'use strict';
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        // we could just concatenate everything, really
        // but we like to have it the complex way.
        // also, in this way we do not have to worry
        // about putting files in the correct order
        // (the dependency tree is walked by r.js)
        requirejs: {
            compile: {
                // What we do here:
                //  1. we define dependencies else the compilation will fail,
                //     and the call to define won't be rewritten
                //     and we have a big error
                //  2. but then we load plone.mockup also in the live site,
                //     and this will result in double-loading
                //     all the dependencies with catastrophic effects
                //     (global states and registries will be rewritten,
                //     nothing will work)
                //  3. So we stub out every single dependency.
                //  4. Result: 10 lines of code to do absolutely nothing.
                //     Amazing :)
                options: {
                    baseUrl: "./",
                    paths: {
                        "bootstrap-carousel": "bower_components/bootstrap/js/carousel"
                    },
                    name: "js/barceloneta",
                    out: "plonetheme/barceloneta/static/barceloneta.js",
                    optimize: "none"
                }
            }
        },
        less: {
            dist: {
                options: {
                    paths: ['bower_components/...'],
                    strictMath: false,
                    sourceMap: true,
                    outputSourceFiles: true,
                    sourceMapURL: '++resource++plonetheme.barceloneta/barceloneta.css.map',
                    sourceMapFilename: 'plonetheme/barceloneta/static/barceloneta.css.map'
                },
                files: {
                    'plonetheme/barceloneta/static/barceloneta.css': 'less/barceloneta.less',
                    'less/barceloneta.css': 'less/barceloneta.less'
                }
            }
        },
        copy: {
            barceloneta: {
                files: [
                    { expand: true, cwd: 'less/images/', src: 'barceloneta-*', dest: 'plonetheme/barceloneta/static/' },
                    { expand: true, cwd: 'less/fonts/', src: 'barceloneta-*', dest: 'plonetheme/barceloneta/static/' }
                ]
            }
        },
        sed: {
          'barceloneta-images': {
            path: 'plonetheme/barceloneta/static/barceloneta.css',
            pattern: 'url\\(\'images/barceloneta-',
            replacement: 'url(\'++resource++plonetheme.barceloneta-'
          },
          'barceloneta-fonts': {
            path: 'plonetheme/barceloneta/static/barceloneta.css',
            pattern: 'url\\(\'fonts/barceloneta-',
            replacement: 'url(\'++resource++plonetheme.barceloneta-'
          }
        },
        watch: {
            scripts: {
                files: ['less/*.less', 'js/*.js'],
                tasks: ['less', 'sed', 'requirejs']
            }
        },
        browserSync: {
            dev: {
                bsFiles: {
                    src : ['plonetheme/barceloneta/static/*.css',]
                },
                options: {
                    watchTask: true,
                    debugInfo: true,
                    server: {
                        baseDir: "."
                    },
                }
            }
        },
        // To use browser-sync directly with Plone you should serve Plone
        // through a web server e.g. Nginx or Apache with VH enabled.
        // If not, then the links are broken because of the proxy made by
        // BrowserSync
        PloneBrowserSync: {
            dev: {
                bsFiles: {
                    src : ['plonetheme/barceloneta/static/*.css',]
                },
                options: {
                    watchTask: true,
                    debugInfo: true,
                    proxy: "http://localhost:8081"
                }
            }
        }
    });

    // grunt.loadTasks('tasks');
    grunt.loadNpmTasks('grunt-browser-sync');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-requirejs');
    grunt.loadNpmTasks('grunt-sed');
    grunt.registerTask('default', ['watch']);
    grunt.registerTask('bsync', ["browserSync", "watch"]);
    grunt.registerTask('plone-bsync', ["PloneBrowserSync", "watch"]);
};
