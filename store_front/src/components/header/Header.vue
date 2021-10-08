<template>
  <div class="header">
    <h1> hello world </h1>
    <input type="search" class="searchInput" placeholder="what are you searching for " />
    <input class="submitButton" type="submit" >
    <nav>
    </nav>
  </div>
</template>

<script>
export default {
  name:'Header'

}
</script>


<style scoped>
.header {
  height: 25%;
  width: 100%;
  background-color: brown;
}

.searchInput{
  width:25%;
  height: 30px;
  border-top-left-radius: 5px;
  border-bottom-left-radius: 5px;
  text-align: center;
  font-size: 1em;
  border-right: none;
  
}

.submitButton {
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
  border-left: none;
  height: 30px;
  font-size: 1em;
  background-color: whitesmoke;
}

</style>