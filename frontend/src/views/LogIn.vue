<template>
    <div id="log-in">
        <LogInHeader></LogInHeader>
        <LogInForm />
    </div>
</template>

<script>

import LogInHeader from "@/components/LogInHeader"
import LogInForm from "@/components/LogInForm"

  export default {
    name: "LogIn",
    components: {
      LogInHeader, LogInForm
    }
  }
</script>

<style scoped>

</style>