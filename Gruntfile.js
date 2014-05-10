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
                options: {
                    baseUrl: "./",
                    paths: {
                        'bootstrap-carousel': 'bower_components/bootstrap/js/carousel'
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
                    paths: ['bower_components/...', '../mockup/bower_components', '../mockup/less'],
                    strictMath: false,
                    sourceMap: true,
                    outputSourceFiles: true,
                    sourceMapURL: '++resource++plonetheme.barceloneta/barceloneta.css.map',
                    sourceMapFilename: 'plonetheme/barceloneta/static/barceloneta.css.map'
                },
                files: {
                    'plonetheme/barceloneta/static/barceloneta.css': 'less/barceloneta.less',
                    'less/barceloneta.css': 'less/barceloneta.less',
                    '../mockup/build/plone.min.css': '../mockup/less/plone.less',
                }
            }
        },
        copy: {
            barceloneta: {
                files: [
                    { expand: true, cwd: 'less/images/', src: 'barceloneta-*', dest: 'plonetheme/barceloneta/static/' },
                    { expand: true, cwd: 'less/fonts/', src: 'barceloneta-*', dest: 'plonetheme/barceloneta/static/' },
                    { expand: true, cwd: 'bower_components/bootstrap/', src: 'fonts/**', dest: 'plonetheme/barceloneta/static/vendor/bootstrap/' }
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
          },
          'bootstrap-fonts': {
            path: 'plonetheme/barceloneta/static/barceloneta.css',
            pattern: 'url\\(\'../bower_components/bootstrap/dist/',
            replacement: 'url(\'++resource++plonetheme.barceloneta.vendor/bootstrap/'
          },
          'plone-fonts': {
            path: '../mockup/build/plone.min.css',
            pattern: 'url\\(\'fonts/plone-',
            replacement: 'url(\'++resource++plone-'
          }
        },
        watch: {
            scripts: {
                files: ['less/*.less', 'js/*.js', '../mockup/less/*.less'],
                tasks: ['less', 'sed', 'requirejs']
            }
        },
        browserSync: {
            html: {
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
            },
            plone: {
                bsFiles: {
                    src : ['plonetheme/barceloneta/static/*.css',]
                },
                options: {
                    watchTask: true,
                    debugInfo: true,
                    proxy: "localhost:8080"
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
    grunt.registerTask('bsync', ["browserSync:html", "watch"]);
    grunt.registerTask('plone-bsync', ["browserSync:plone", "watch"]);
};
