<template>
    <header>
        <img src="@/assets/todo-icon.png" alt="todo-icon" id="logo-icon">
        <span id="logo">ToDo List</span>
    </header>
</template>

<script>
  export default {
    name: "LogInHeader"
  }
</script>

<style scoped>
    header {
        font-size: 22px;
        display: flex;
        background-color: #6564DB;
        width: 100%;
        height: 3.55em;
    }

    @media (min-width: 2000px) {
        header {
            font-size: 26px;
        }
    }

    @media (min-width: 2300px) {
        header {
            font-size: 28px;
        }
    }

    #logo {
        font-family: 'Poppins', sans-serif;
        margin-left: 0.625em;
        margin-top: 0.925em;
    }

    #logo-icon {
        margin-left: 0.625em;
        margin-top: 0.625em;
        width: 2em;
        height: 2em;
    }
</style>