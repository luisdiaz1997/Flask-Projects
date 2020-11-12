<template>
    <div id="analyze-quote">

        <div v-if="!quote">
            <h2>Analyze Text</h2>
            <br>
        </div>
        <b-row>
            <b-col cols="5">
                <div v-if="quote" class="quote">
                    <div class="quote_text">
                        <p>{{quote.text}}</p>
                    </div>
                </div>
                <div v-else>
                    <b-form-textarea
                    id="textarea"
                    v-model="text"
                    placeholder="Enter something..."
                    rows="5"
                    max-rows="10"
                    ></b-form-textarea>
                </div>
            </b-col>
            <b-col cols="2">
                <b-form-select
                v-model="language"
                :options="languages"
                required
                ></b-form-select>
                <br>
                <br>
                <b-button v-if="text || quote" variant="primary" @click="translateText">Translate</b-button>
                <br>
                <br>
                <b-button v-if="text || quote" variant="primary" @click="get_audio"> Play audio</b-button>

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
export default {
    name: "AnalyzeQuote",
    props:{
        quote: Object
    },
    data()
    {
        return{
            languages:['Spanish', 'English'],
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
            let text = this.quote? this.quote.text: this.text
            formData.append('text', text)
            let config=  { 
                headers: {
                'Content-Type': 'multipart/form-data'
                }
            }
            this.$api.post('/analyze_text', formData, config).then((response)=>{
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
        this.$api.post('/text_to_audio', formData, config).then((response)=>{
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
.quote{
    background-color: khaki;
    height: 75%;
    border-radius: 10px;
    box-shadow: 10px 5px 5px slategrey;
}
.quote_text{
        display: flex;
        height: 100%;
        margin: auto;
        align-items:center;
        justify-content:center;

}

</style>