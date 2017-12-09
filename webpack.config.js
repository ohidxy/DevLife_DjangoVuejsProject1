const path = require('path')

module.exports = {
  entry: {
    index: ['./devlife/static/src/index.js', /* './devlife/static/src/index.scss' */ ]
  },
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
    ]
  }
}