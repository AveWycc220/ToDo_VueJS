<template>
    <div class="main-page">
        <MainHeader></MainHeader>
    </div>
</template>

<script>
import MainHeader from "@/components/MainPage/MainHeader";
import CookieUtils from "@/cookieUtils/cookieUtils";
import Api from "@/api/Api";

  export default {
    name: "MainPage",
    components: {
      MainHeader
    },
    data() {
      return {
        itemList: undefined
      }
    },
    beforeCreate() {
      if (CookieUtils.getCookie('auth') === '1') {
        Api.getData({login:false}).then((data) => { this.itemList = JSON.parse(JSON.stringify(data)) })
      } else {
        this.$router.push('/login')
      }
    },
  }
</script>

<style scoped>

</style>