<template>
    <div id="DataUploader">
        I'll upload your data
       

        <b-container>
            <b-row>
                <b-col>
                     
                        <img v-if="image" alt="Uploaded image" class="imgStyle" :src="getImPreview()">
                        <img v-else alt="Vue logo" class="imgStyle" src="../assets/logo.png">

                </b-col>

                <b-col class="vcenter-content">
                    
                    <b-form-file
                    v-model="image"
                    :state="Boolean(image)"
                    placeholder="Choose a file or drop it here..."
                    drop-placeholder="Drop file here..."
                    ></b-form-file>
                    <div class="mt-3">Selected file: {{ image ? image.name : '' }}</div>
                    
                    
                </b-col>
                
            </b-row>
            <b-row>
                <b-col>1 of 2</b-col>
                <b-col>2 of 2</b-col>
            </b-row>
        </b-container>
    </div>
</template>


<script>
export default {
  name: 'DataUploader',
  props: {
    msg: String
  },
  data(){
    return{
        image:null
    }
  },
  methods:
  {
        getImPreview()
        {
            return URL.createObjectURL(this.image);
        }
  }


}
</script>


<style scoped>
.imgStyle{
    object-fit: contain;
    object-position: center;
    height: 400px;
    width: 100%;
}

.vcenter-content{
   margin-top:auto;
   margin-bottom:auto;
   /* display:block; */

}
</style>