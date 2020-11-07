<template>
    <header><span id="logo">ToDo List</span></header>
</template>

<script>
  export default {
    name: "Header"
  }
</script>

<style scoped>
    header {
        display: flex;
        background-color: #ff6800;
        width: 100%;
        height: 60px;
    }

    #logo {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        margin-left: 10px;
        margin-top: 10px;
    }
</style>