<template>
    <div id="text-uploader">

        <h2>Analyze Text</h2>
            <br>
        <b-row>
            <b-col cols="5">
                    <b-form-textarea
                    id="textarea"
                    v-model="text"
                    placeholder="Enter something..."
                    rows="5"
                    max-rows="10"
                    ></b-form-textarea>
            </b-col>
            <b-col cols="2">
                <b-form-select
                v-model="language"
                :options="languages"
                required
                ></b-form-select>
                <br>
                <br>
                <b-button v-if="text" variant="primary" @click="translateText">Translate</b-button>
                <br>
                <br>
                <b-button v-if="text" variant="primary" @click="get_audio"> Play audio</b-button>

            </b-col>
            <b-col cols="5">
                 <b-alert v-model="showDismissibleAlert" variant="danger" dismissible>
                    <p>Please select language</p>
                </b-alert> 
                <p v-if="translation">{{translation}}</p>   
            </b-col>
        </b-row>
    </div>
</template>
<script>
import axios from "axios";
export default {
    name: "TextUploader",
    data()
    {
        return{
            languages:['Spanish', 'Italian', 'Portuguese', 'Italian'],
            language:null,
            text:null,
            showDismissibleAlert: false,
            translation:null

        }
    },
    methods:
    {
        translateText()
        {
            if (this.language===null)
            {
                this.showDismissibleAlert=true
                // alert("Please select Language")
                return;
            }
            let formData = new FormData();
            formData.append('language', this.language)
            formData.append('text', this.text)
            let config=  { 
                headers: {
                'Content-Type': 'multipart/form-data'
                }
            }
            axios.post('http://127.0.0.1:5000/analyze_text', formData, config).then((response)=>{
                this.translation = response.data["message"]
                })
        }
            ,
        get_audio()
        {
        let formData = new FormData();
        formData.append('text',  this.text);
        let config=  { 
            headers: {
            'Content-Type': 'multipart/form-data'
            }
        }
        axios.post('http://127.0.0.1:5000/text_to_audio', formData, config).then((response)=>{
            console.log(response)
            
            })
        }
    }
    
}
</script>

<style scoped>

#text-uploader{
    margin-bottom: 50px;
    margin-top: 50px;
}

</style>