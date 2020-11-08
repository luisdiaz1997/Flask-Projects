<template>
  <div class="home">
    
    <b-container>
      <DataUploader :image="image" @changed-image="updateImage"/>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import DataUploader from '@/components/DataUploader.vue'

export default {
  name: 'Home',
  components: {
    DataUploader
  },
  methods:
  {
    updateImage(newImage){
      this.image=newImage
      this.$store.commit('replaceImage', this.image)
    }
  },
  data(){
    return{
      image:null
    }
  },
  mounted(){
    this.image = this.$store.state.image
  }
}
</script>
