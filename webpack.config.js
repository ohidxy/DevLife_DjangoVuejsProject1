const path = require('path')
const ExtractTextPlugin = require('extract-text-webpack-plugin')
const srcDir = path.resolve(__dirname, './devlife/static/src')

function getPostcssLoaderPlugins () {
  return [require('precss'), require('autoprefixer')]
}
const postcssLoaderOptions = {
  plugins: getPostcssLoaderPlugins
}
const sassLoaderOptions = {
  includePaths: [srcDir]
}

const fileLoaderOptions = {
  name: '[path][name].[ext]',
  context: './devlife/static/src'
}

module.exports = {
  entry: {
    index: ['./devlife/static/src/index.js', './devlife/static/src/index.scss']
  },
  watch: true,
  output: {
    path: path.resolve(__dirname, './devlife/static/dist'),
    filename: 'index.js'
  },
  resolve: {
    alias: {
      vue: 'vue/dist/vue.js'
    }
  },
  module: {
    loaders: [
      {
        test: /\.js?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets:['env']
        }
      },

      {
        test: /\.vue$/,
        loader: 'vue-loader',
        query: {
          presets:['env']
        }
      },
      // Handle css and scss files
      {
        test: /\.(scss|css)$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
            'css-loader',
            {loader: 'postcss-loader', options: postcssLoaderOptions},
            {loader: 'sass-loader', options: sassLoaderOptions}
          ]
        })
      },
      
      // Handle fonts
      {
        test: /\.(svg|woff2?|ttf|eot)(\?v=\d+\.\d+\.\d+)?$/,
        loaders: [
          {
            loader: 'file-loader',
            options: Object.assign({}, fileLoaderOptions, {
              name: 'fonts/[name].[ext]'
            })
          }
        ]
      },

    ]
  },

  plugins: [ 
    new ExtractTextPlugin( "index.css" )
  ]
}