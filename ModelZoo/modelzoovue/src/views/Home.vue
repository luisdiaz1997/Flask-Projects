<template>
  <div class="home">
    <b-row>
      <b-col>
      </b-col>
      <b-col cols="8">
        <Numbers />
      </b-col>
      <b-col>
      </b-col>
    </b-row>
      
  </div>
</template>

<script>
import Numbers from "@/components/Numbers.vue";
// @ is an alias to /src
export default {
  name: "Home",
  components: {
    Numbers
  }
};
</script>
