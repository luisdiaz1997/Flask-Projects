<template>
    <div id="text-uploader">
        <h2>Type your own quote</h2>
        <b-form-textarea
            id="textarea"
            v-model="text"
            placeholder="Enter something..."
            rows="5"
            max-rows="10"   
        ></b-form-textarea>
        <b-button variant="primary" @click="saveText">Upload Quote</b-button>
        <b-alert v-model="uploaded" variant="success" dismissible>
            <p>You can check your quote in <router-link to="/">Home</router-link></p>
        </b-alert> 
    </div>
</template>
<script>
export default {
    name: "TextUploader",
    data(){
        return{
            text: null,
            uploaded: false
        }
    },
    methods:{
        saveText(){
            let formData = new FormData();
            formData.append('text', this.text);
            let config=  { 
                headers: {
                'Content-Type': 'multipart/form-data'
                }
            }
            this.$api.post('/save_text', formData, config).then((response)=>{
                console.log(response.data)
                this.uploaded = true
            })
        }
    }
}
</script>

<style scoped>
#text-uploader{
    margin-top: 20px;
}

</style>