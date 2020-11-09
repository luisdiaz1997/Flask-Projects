<template>
  <div class="home">
    
    <b-container>
      <ImageUploader :image="image" @changed-image="updateImage"/>
      <AudioUploader/>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import ImageUploader from '@/components/ImageUploader.vue'
import AudioUploader from '@/components/AudioUploader.vue'


export default {
  name: 'Home',
  components: {
    ImageUploader,
    AudioUploader
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
