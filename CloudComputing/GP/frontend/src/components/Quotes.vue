<template>
    <div id="quotes">

        <div v-if="loading">
            <b-skeleton-img></b-skeleton-img>
        </div>
        <div v-else>
            <div v-for="quote in quotes" :key="quote.id">
                <TextUploader :quote="quote"/>
            </div>
        </div>
        
    </div>
    
</template>
<script>
import TextUploader from './TextUploader.vue'

export default {
    name: "Quotes",
    components:{TextUploader},
    props: {
        quotes: Array,
        loading: Boolean
    }
    
}
</script>

<style scoped>

</style>