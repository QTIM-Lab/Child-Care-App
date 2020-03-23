<template>
  <div class="container">
    <!-- NavBar -->
    <NavBar></NavBar>
    <!-- <div class="jumbotron">
    </div> -->
    <div class="row">
      <h1>MGH Community Help</h1>
      <iframe src="https://www.google.com/maps/d/u/1/embed?mid=1JsA5_X7Kk0ejNZvo1hOJPRL9bPnCq_eh" width="100%" height="480"></iframe>
      <p>Edit this map
        <a href="https://drive.google.com/open?id=1JsA5_X7Kk0ejNZvo1hOJPRL9bPnCq_eh&usp=sharing">
        here
        </a>
      </p>
    </div>
    <br>
    <ChildCareRequests></ChildCareRequests>
    <br>
    <br>
    <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSc607Obx7cgTqDECsR9wO280rucBdnyCH_PibUeLrVh2CPRmg/viewform?embedded=true" width="640" height="1517" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
  </div>
</template>

<script>
// import Parallax from 'vue-parallaxy';
import ChildCareRequests from './ChildCareRequests.vue';
import NavBar from './NavBar.vue';


export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
  components: {
    ChildCareRequests,
    NavBar,
    // Parallax,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */

body {
  width: 100vw;
  height: 100vh;
  margin: 0 0 0 0;
  background-color: #f3f3f3; }

h1 {
  color: #000;
  /* From Google Fonts */
  /* margin: auto; */
  /* width: 50%; */
  line-height: 75px;
  display: inline;
  /* font-size: xxx-large; */
  text-align: left;
  /* font-family: 'Odibee Sans'; */
}

p {
  display: block;
}
</style>
