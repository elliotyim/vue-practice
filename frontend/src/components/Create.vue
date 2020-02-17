<template>
  <div>
    <v-container>
        <v-row>
          <h1>Posting</h1>
          <v-col cols="12" md="6">

            <v-text-field 
              outlined
              label="Title"
              v-model="title"
              /><br/>
            <v-textarea
              outlined
              no-resize
              name="input-7-4"
              label="Content"
              v-model="content"
            ></v-textarea><br/>
            <v-text-field
              outlined
              label="Author"
              v-model="writer"
            />
            <v-btn
              outlined
              color="primary"
              @click="index !== undefined ? update() : write()"
            >
              {{index !== undefined ? 'Update' : 'Delete'}}
            </v-btn>
          </v-col>
        </v-row>
    </v-container>
  </div>
</template>
<script>
import data from '@/data';

export default {
    name: 'Create',
    data() {
      const index = this.$route.params.contentId;
        return {
            data: data,
            index: index,
            title: index !== undefined ? data[index].title : "",
            content: index !== undefined ? data[index].content : "",
            writer: index !== undefined ? data[index].writer : "",
        }
    },
    methods: {
        write() {
          this.data.push({
              title: this.title,
              content: this.content,
              writer: this.writer,
          });
          this.$router.push({
              path: '/'
          })
        },
        update() {
          data[this.index].title = this.title;
          data[this.index].content = this.content;
          data[this.index].writer = this.writer;
          this.$router.push({
            path: '/'
          })
        }
    }
}
</script>