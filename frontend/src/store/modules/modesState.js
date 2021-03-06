import ajax from '../../axios.config'
import Vue from 'vue'

const modesState = {
    namespaced: true,
    state: {
        modes: [],
        currentMode: null
    },
    getters: {
        modes: state => state.modes,
        currentMode: state => state.currentMode,
        currentModeById: state => modeId => {
            return state.modes.filter(item => item.id == modeId)[0]
        }
    },
    mutations: {
        SET_MODES (state, modes) {
            state.modes = modes;
        },
        ADD_MODES (state, mode) {
            state.modes.push(mode);
        },
        SET_CURRENT_MODE (state, modeId) {
            state.currentMode = modeId ? state.modes.filter(item => item.id == modeId)[0] : null
        },
        UPDATE_CURRENT_MODE (state, mode) {
            state.currentMode = mode
        },
        CHANGE_CELL_VALUE (state, cellData) {
            let currentMode = JSON.parse(JSON.stringify(state.currentMode))
            currentMode.fields = currentMode.fields.map(item => {
                if (item['table_name'] === cellData.tableName && item['name'] === cellData.name) {
                    item[cellData.dataType] = +cellData.value
                    return item
                }
                else return item
            })

            state.currentMode = currentMode
        },
        DELETE_CELL (state, cellData) {
            let currentMode = JSON.parse(JSON.stringify(state.currentMode))
            currentMode.fields = currentMode.fields.filter(item => {
                if (item['table_name'] === cellData.tableName && item['name'] === cellData.name) {
                    return null
                }
                else return item
            })

            state.currentMode = currentMode
        },
        ADD_NEW_CELL (state, cellData) {
            let currentMode = JSON.parse(JSON.stringify(state.currentMode))
            currentMode.fields.push({
                'table_name': cellData.tableName,
                'name': cellData.name,
                'min_normal': '',
                'max_normal': ''
            })

            state.currentMode = currentMode
        },
        CANCEL_MODE (state, modeId) {
            state.currentMode = state.modes.filter(item => item.id == modeId)[0]
        }
    },
    actions: {
        getModes ({ commit, state, getters }, payload) {
            return ajax.get(window.HOSTNAME+'/api/bl/modes_api/', {
                withCredentials: true
            })
                .then(response => {
                    commit('SET_MODES', response.data)
                })
                .catch(e => {
                    console.log(e)
                });
        },
        addMode ({ commit, state, getters }, payload) {
            return ajax.post(window.HOSTNAME+'/api/bl/modes_api/', {
                message: payload.mode.message,
                plant: payload.mode.plant,
                journal: payload.mode.journal,
                fields: payload.mode.fields.map(item => {
                    return {
                        table_name: item.table_name,
                        name: item.name,
                        min_normal: item.min_normal,
                        max_normal: item.max_normal
                    }
                })
            }, {
                withCredentials: true
            })
                .catch(e => {
                    console.log(e)
                });
        },
        toggleMode ({ commit, state, getters }, payload) {
            return ajax.put(window.HOSTNAME+'/api/bl/modes_api/', { id: payload.modeId, is_active: payload.isActive }, {
                withCredentials: true
            })
                .catch(e => {
                    console.log(e)
                });
        },
        deleteMode ({ commit, state, getters }, payload) {
            return ajax.delete(window.HOSTNAME+`/api/bl/modes_api/${payload.modeId}`, {
                withCredentials: true
            })
                .catch(e => {
                    console.log(e)
                });
        },
        updateMode ({ commit, state, getters }, payload) {
            return ajax.put(window.HOSTNAME+`/api/bl/modes_api/`, payload, {
                withCredentials: true
            })
                .catch(e => {
                    console.log(e)
                });
        }
    }
}

export default modesState
