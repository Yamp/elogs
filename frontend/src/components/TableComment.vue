<template>
    <div class="table__comment">
        <div v-if="mode==='edit'">
          <a href="javascript:;" @click="onClick()">Комментарий</a>
          <div :class="['comment__text', { collapse: isCollapsed }]">
              <textarea
                      class="table-comment"
                      placeholder="Комментарий..."
                      title=""
                      :value="text"
                      @input="onInput"
                      ref="comment_input"
              >
              </textarea>
          </div>
        </div>
        <div v-else>
            <template v-if="text">
                <b>Комментарий:</b> {{ text }}
            </template>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'table-comment',
        props: ['tableName'],
        data() {
            return {
                rowIndex: '0',
                isCollapsed: true,
                fieldName: '__table__comment'
            }
        },
        watch: {
            text(value) {

            }
        },
        computed: {
            mode() {
                return this.$store.state.journalState.journalInfo.mode;
            },
            text: {
                get: function () {
                    return this.$store.getters['journalState/cell'](this.tableName, this.fieldName, this.rowIndex)['value']
                },
                set: function (val) {
                    this.$store.commit('journalState/SAVE_CELLS', {
                        'cells': [{
                            tableName: this.tableName,
                            fieldName: this.fieldName,
                            responsible: {[this.$store.getters['userState/username']]: this.$store.getters['userState/fullname']},
                            index: this.rowIndex,
                            value: val,
                        }]
                    });
                }
            }
        },
        methods: {
            onInput(e) {
                this.text = e.target.value;
                this.send()
            },
            onClick() {
                this.isCollapsed = !this.isCollapsed;
                if (!this.isCollapsed) {
                    this.$nextTick(() => {
                        this.$refs.comment_input.focus();
                    })
                }
            },
            send() {
                this.$socket.sendObj({
                    'type': 'shift_data',
                    'cells': [{
                        'cell_location': {
                            'group_id': this.$store.getters['journalState/journalInfo'].id,
                            'table_name': this.tableName,
                            'field_name': this.fieldName,
                            'index': this.rowIndex
                        },
                        'value': this.text || ''
                    }]
                });
            }
        },
        mounted() {
            if (this.text) {
                this.isCollapsed = false;
            }
        }
    }
</script>
<style scoped>
    .ico-comment {
        margin-left: 5px;
    }
</style>
