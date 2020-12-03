<template>
    <div class="main-page">
        <Loading v-if="loading"></Loading>
        <MainHeader v-else></MainHeader>
    </div>
</template>

<script>
import MainHeader from "@/components/MainPage/MainHeader";
import Api from "@/api/Api";
import Loading from "@/components/Loading";

  export default {
    name: "MainPage",
    components: {
      MainHeader, Loading
    },
    data() {
      return {
        itemList: undefined,
        loading: true
      }
    },
    mounted() {
      if (this.$cookie.get('auth') === '1') {
        Api.getData({login:false}).then((data) => {
          this.itemList = JSON.parse(JSON.stringify(data))
          this.loading = false
        })
      } else {
        this.$router.push('/login')
      }
    }
  }
</script>

<style scoped>

</style>