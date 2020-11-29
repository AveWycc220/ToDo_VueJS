<template>
  <div id="app">
    <LogIn></LogIn>
  </div>
</template>

<script>

import LogIn from "@/views/LogIn"

export default {
  name: 'App',
  components: {
    LogIn
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin: 0;
  padding: 0;
}
</style>
