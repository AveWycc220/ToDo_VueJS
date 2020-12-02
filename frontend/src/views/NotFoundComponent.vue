<template>
   <div>
      <p>Error 404 - Page Not Found</p>
      <p>The page you were looking for wasn't found</p>
   </div>
</template>

<script>
  export default {
    name: "NotFoundComponent"
  }
</script>

<style scoped>
   div {
      font-size: 20px;
      width: 30em;
      height: 20em;
      position: relative;
      margin: 12em auto;
   }

   p {
      font-family: 'Poppins', sans-serif;
      text-align: center;
   }

   @media (max-width: 875px) {
      div {
         font-size: 18px;
      }
   }

   @media (max-width: 575px) {
      div {
         font-size: 10px;
      }
   }

   @media (min-width: 2000px) {
      div {
         font-size: 28px;
      }
   }
</style>