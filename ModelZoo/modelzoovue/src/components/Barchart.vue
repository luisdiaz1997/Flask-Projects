<template>
  <div id="barchart">
    <div v-for="(label, index) in labels" :key="index" class="element">
        <div class="bar" :style="{background: 'white', height: 100*((1-predictions[index]))  + 'px'}"/>
        <div class="bar" :style="{background: 'blue', height: 100*(predictions[index])  + 'px'}"/>
        {{label}}
    </div>
  </div>
</template>

<script>
export default {
    name: "Barchart",
    props: { labels: Array, predictions: Array},
    computed:{
        
    }

}
</script>

<style scoped>
#barchart{
    overflow-y: hidden;
}
.element{
    float: left;
    margin: 0.2em;
    bottom: 0;
}
.bar{
    width: 20px;
}
</style>