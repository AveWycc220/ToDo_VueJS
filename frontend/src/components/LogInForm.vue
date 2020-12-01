<template>
    <div class="form">
        <div class="key-input">
            <p class="help-text" v-if="hasError"> {{ errorMessage }} </p>
            <div>
                <form @submit.prevent="login">
                    <input type="text" id="key-input" name="key" placeholder="Key for your task list" maxlength="200"
                           v-model="key" :style="{ border: styleForInput }">
                </form>
            </div>
            <div class="info">
                <p class="help-text" v-if="checkForCharacters">These symbols are prohibited: &lt;, >, :, ", /, \, |, ?, *</p>
                <p class="help-text" v-if="checkForLength">Key is too long (Must be less then 200 symbols)</p>
            </div>
        </div>
        <div class="button-div">
            <button class="open-button" :disabled="disableButton" @click="login">Open List / Create New List</button>
        </div>
    </div>
</template>

<script>
  import Api from "@/api/Api"

  export default {
    name: "LogInForm",
    data() {
      return {
        key: '',
        errorMessage: '',
      }
    },
    methods: {
      login() {
        if (!!this.key && !this.checkForCharacters && !this.checkForLength) {
          console.log(`Connect to http://${process.env.VUE_APP_SERVER_DOMAIN}:${process.env.VUE_APP_SERVER_PORT}`)
          Api.login(this.key).then((data) => {
            if (typeof data === 'object') {
              this.errorMessage = ''
              console.log(data)
            } else if (typeof data === 'number') {
              this.errorMessage = `Error, HTTP Status = ${data}`
            } else if (typeof data === 'boolean') {
              this.errorMessage = 'Server doesnt work | Wrong PORT or DOMAIN'
            }
          })
        }
      }
    },
    computed: {
      styleForInput() {
        return this.key && !this.checkForCharacters && !this.checkForLength ? '2px solid green' : '2px solid red'
      },
      checkForCharacters() {
        let listCharacters = ['<', '>', ':', '/', '\\', '|', '?', '*']
        let res = false
        for (let item of listCharacters) {
            res ||= !!~this.key.indexOf(`${item}`)
        }
        return res
      },
      checkForLength() {
        return this.key.length === 200
      },
      disableButton () {
        return !(!!this.key && !this.checkForCharacters && !this.checkForLength)
      },
      hasError() {
        return !!this.errorMessage
      }
    },
  }
</script>

<style scoped>
    .form {
        display: flex;
        flex-direction: column;
        background-color: #ffffff;
        width: 20em;
        height: 22.25em;
        margin: 10em auto;
        border-radius: 10px;
        -webkit-box-shadow: 0 1px 13px 0 rgba(50, 50, 50, 0.7);
        -moz-box-shadow: 0 1px 13px 0 rgba(50, 50, 50, 0.7);
        box-shadow: 0 1px 13px 0 rgba(50, 50, 50, 0.7);
    }

    .key-input {
        flex: 1;
        margin: 5em auto;
    }

    .help-text {
        margin-top: 1em;
        margin-bottom: 1em;
        color: red;
        font-size: 11px;
        text-align: center;
    }

    .open-button {
        background: #2431e2;
        color: #ffffff;
        border: none;
        text-align: center;
        text-decoration: none;
        font-size: 14px;
        flex: 1;
        border-radius: 10px;
        width: 15em;
        height: 2.5em;
        margin-bottom: 0.75em;
        position: relative;
        left: 50%;
        transform: translate(-50%, 0);
        transition-property: background;
        transition-duration: .5s;
    }

    .open-button:hover{
        background: #434bff;
        cursor: pointer;
    }

    .open-button:active,
    .open-button:focus {
        outline: none;
        background: #b2c4ff;
    }

    .button-div {
        margin: auto auto 15em;
    }

    input {
        width: 18em;
        border: 2px solid red;
        border-radius: 4px;
        padding: 0.8em 0.8em;
    }

    input:active, input:hover, input:focus {
        outline: 0;
        outline-offset: 0;
    }

    @media (max-width: 875px) {
        .form {
            font-size: 14px;
        }
        input {
            font-size: 12px;
        }
        .open-button{
            font-size: 12px;
        }
    }

    @media (min-width: 2000px) {
        .form {
            font-size: 22px;
        }
        input {
            font-size: 20px;
        }
        .open-button{
            font-size: 20px;
        }
    }

    @media (min-width: 2300px) {
        .form {
            font-size: 24px;
        }
        input {
            font-size: 22px;
        }
        .open-button {
            font-size: 22px;
        }
    }

</style>