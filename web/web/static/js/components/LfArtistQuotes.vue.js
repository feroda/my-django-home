import { nextTick } from 'vue';

export default {
  name: 'LfArtistQuotes',
  emits: [],
  props: {},
  data() {
    return {
      artistquotes: [],
      loading: false,
    }
  },
  mounted: async function () {
      console.log(`${this.$options.name}: mounted...`);
      await this.loadItems();
  },
  methods: {
    async loadItems() {
      console.log(`${this.$options.name}: sto caricando...`);
      this.loading = true;
      await nextTick();
      const jsonDoc = await window.http.doHttpGETJson(`v1/artistquotes/`);
      console.debug(`${this.$options.name}: total=${jsonDoc.count}; ultimo risultato di seguito.`);
      if (jsonDoc.results) {
        console.debug(jsonDoc.results[jsonDoc.results.length - 1]);
      }
      this.artistquotes.splice(0, this.artistquotes.length);
      this.artistquotes.push(...jsonDoc.results);

      // set loading to false after 0.5sec to avoid quick reload
      setTimeout(() => {
        this.loading = false;
      }, 500); //
    }
  },
  template: /*html*/`
  <div
    class="item-group d-flex ga-3 ma-4"
    xyz="fade origin-top-left perspective-2 left-5 stagger-3"
  >
    <v-card
        class="mx-auto w-25"
        :subtitle="aq.artist"
        :title="aq.title"
        v-for="aq in artistquotes"
      >
        <template v-slot:prepend>
          <v-avatar color="blue-darken-2" v-if="aq.sub_avatar !== null">
            <v-img
              :alt="aq.artist"
              :src="aq.sub_avatar"
            ></v-img>
          </v-avatar>
        </template>
        <template v-slot:append>
          <v-avatar size="24" v-if="aq.main_avatar !== null">
            <v-img
              :alt="aq.title"
              :src="aq.main_avatar"
            ></v-img>
          </v-avatar>
        </template>
        <v-card-text class="font-italic">{{ aq.body }}</v-card-text>
    </v-card>
  </div>
  `
};
