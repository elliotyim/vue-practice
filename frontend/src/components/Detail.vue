<template>
    <div>
        <div>{{ data.title }}</div>
        <div>{{ data.content }}</div>
        <div>{{ data.writer }}</div>
        <button @click="updateData">Update</button>
        <button @click="deleteData">Delete</button>
    </div>
</template>
<script>
import data from '@/data';
export default {
    name: 'Detail',
    data() {
        const index = this.$route.params.contentId;
        return {
            data: data[index],
            index: index
        }
    },
    methods: {
        deleteData() {
            console.log(this.index);
            data.splice(this.index, 1);
            this.$router.push({
                path: '/'
            })
        },
        updateData() {
            this.$router.push({
                name: 'Create',
                params: {
                    contentId: this.index
                }
            });
        }
    }
}
</script>