<template>
  <div class="header d_flex">
    <h1 class="header_title">Hello world </h1>
    <div class="input_wrapper">
    <input type="search" class="searchInput" placeholder="what are you searching for " />
    <input class="submitButton" type="submit" >
    </div>
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
}

.d_flex {
  display: flex;
  justify-content: space-between ;
}

.header_title {
  margin:1.5%;
}


.input_wrapper{
  height: 100%;
  width:100%;
}
.searchInput{
  margin-top:2%;
  width:25%;
  height: 30px;
  border-top-left-radius: 5px;
  border-bottom-left-radius: 5px;
  text-align: center;
  font-size: 1em;
  border-right: none;
  
}

.submitButton {
  margin-top:2%;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
  border-left: none;
  height: 30px;
  font-size: 1em;
  background-color: whitesmoke;
}

</style>