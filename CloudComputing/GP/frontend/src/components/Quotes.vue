<template>
    <div id="quotes">

        <div v-if="loading">
            <b-skeleton-img></b-skeleton-img>
        </div>
        <div v-else>
            <div v-for="quote in quotes" :key="quote.id">
                <AnalyzeQuote :quote="quote"/>
            </div>
        </div>
        
    </div>
    
</template>
<script>
import AnalyzeQuote from './AnalyzeQuote.vue'

export default {
    name: "Quotes",
    components:{AnalyzeQuote},
    props: {
        quotes: Array,
        loading: Boolean
    }
    
}
</script>

<style scoped>

</style>