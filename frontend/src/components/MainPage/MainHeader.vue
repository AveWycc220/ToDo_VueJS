<template>
    <header>
        <div class="logo-icon">
            <img src="@/assets/to-do-list.svg" alt="todo-icon" id="logo-icon">
        </div>
        <div class="find-div">
            <img src="@/assets/search.svg" alt="find-icon" id="logo-find">
            <input type="text" placeholder="Find Tasks" maxlength="200" id="input-find">
        </div>
        <div class="log-out-div">
            <img src="@/assets/logout.svg" alt="log-out-icon" id="logo-log-out" @click="logout">
        </div>
    </header>
</template>


<script>
  export default {
    name: "MainHeader",
    methods: {
      logout() {
        this.$cookie.set('auth', '0', {maxAge: 604800});
        this.$router.push('/login')
      }
    }
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

    .find-div {
        position: relative;
        margin-top: 1.025em;
        flex: 18;
    }

    .logo-icon {
        flex: 9;
    }

    .log-out-div {
        flex: 1;
    }

    #logo-icon {
        margin-left: 0.625em;
        margin-top: 0.625em;
        width: 2em;
        height: 2em;
    }

    #logo-find {
        width: 1.5em;
        height: 1.5em;
    }

    #logo-log-out {
        padding: 5px;
        margin-top: 0.925em;
        margin-right: 0.5em;
        outline-offset: 1px;
        outline: 3px #6564DB solid;
        -moz-outline-radius: 1px;
        transition-property: outline;
        transition-duration: .3s;
    }

    #logo-log-out:hover {
        cursor: pointer;
        outline: 3px #b8b7f6 solid;
    }

    #input-find {
        position:absolute;
        outline: 0;
        border: 0;
        font-family: 'Poppins', sans-serif;
        font-size: 20px;
        padding-left: 0.25em;
        margin-left: 0.5em;
        margin-top: 0.15em;
        border-radius: 2px;
        width: 8em;
        background: #6564DB;
        color: black;
        transition-property: background;
        transition-duration: .5s;
    }

    #input-find::placeholder {
        font-family: 'Poppins', sans-serif;
        font-size: 20px;
        color: black;
    }

    #input-find:active, #input-find:hover, #input-find:focus {
        outline: 0;
        outline-offset: 0;
    }

    #input-find:hover, #input-find:active, #input-find:focus {
        background: #cccbfa;
    }

    #logo-log-out{
        width: 1.5em;
        height: 1.5em;
    }

    @media (max-width: 875px) {
        header {
            font-size: 14px;
        }
        .find-div {
            font-size: 14px;
        }
        #input-find::placeholder {
            font-size: 14px;
        }
        #input-find {
            font-size: 14px;
        }
    }

    @media (max-width: 575px) {
        header {
            font-size: 10px;
        }
        .find-div {
            font-size: 10px;
        }
        #input-find::placeholder {
            font-size: 10px;
        }
        #input-find {
            font-size: 10px;
        }
    }
    
    @media (max-width: 400px) {
        header {
            font-size: 8px;
        }
        .find-div {
            font-size: 8px;
        }
        #input-find::placeholder {
            font-size: 8px;
        }
        #input-find {
            font-size: 8px;
        }
    }

    @media (min-width: 2000px) {
        header {
            font-size: 26px;
        }
        .find-div {
            font-size: 26px;
        }
        #input-find::placeholder {
            font-size: 26px;
        }
        #input-find {
            font-size: 26px;
        }
    }

    @media (min-width: 2300px) {
        header {
            font-size: 28px;
        }
        .find-div {
            font-size: 28px;
        }
        #input-find::placeholder {
            font-size: 28px;
        }
        #input-find {
            font-size: 28px;
        }
    }
</style>