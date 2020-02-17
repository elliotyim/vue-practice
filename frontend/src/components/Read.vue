<template>
    <div>
        <v-simple-table>
            <thead>
                <tr>
                    <td>Title</td>
                    <td>Content</td>
                    <td>Author</td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(value, index) in data" :key="index" @click="detail(index)">
                    <td>{{ value.title }}</td>
                    <td>{{ value.content }}</td>
                    <td>{{ value.writer }}</td>
                </tr>
            </tbody>
        </v-simple-table>
        <v-btn outlined color="primary" @click="write">Post</v-btn>
    </div>
</template>
<script>
import data from '@/data';

export default {
    name: 'Read',
    data() {
        return {
            data: data
        }
    },
    methods: {
        write() {
            this.$router.push({
                path: 'create'
            });
        },
        detail(index) {
            this.$router.push({
                name: 'Detail',
                params: {
                    contentId: index
                }
            });
        }
    }
}
</script>