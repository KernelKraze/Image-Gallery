const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: '/photo/', // 相当于 Vite 的 base 配置
  // 其他配置...
})
