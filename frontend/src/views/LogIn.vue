<template>
    <div id="log-in">
        <LogInHeader></LogInHeader>
        <LogInForm />
    </div>
</template>

<script>

import LogInHeader from "@/components/LogIn/LogInHeader"
import LogInForm from "@/components/LogIn/LogInForm"

  export default {
    name: "LogIn",
    components: {
      LogInHeader, LogInForm
    }
  }
</script>

<style scoped>

</style>