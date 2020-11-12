<template>
  <div class="about text-center container">
    <h1 class="font-weight-bold">
      This was a project for Cloud Computing at SFSU
    </h1>
    <br />
    <h2 class="font-weight-bold">Authors:</h2>
    <br />

    <h4 v-for="member in members" :key="member">
      {{ member }}
    </h4>
  </div>
</template>

<script>
export default {
  name: "about",
  data() {
    return {
      members: [
        "Luis Chumpitaz",
        "John Gann",
        "Sally Mostafa",
        "Bhavani Goruganthu",
      ],
    };
  },
};
</script>

<style scoped></style>
