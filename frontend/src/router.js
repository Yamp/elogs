import Vue from 'vue/dist/vue.esm.js'
import Router from 'vue-router'
import VueCookies from 'vue-cookies'

import BasePage from './components/BasePage.vue'
import Dashboard from './components/Dashboard.vue'
import JournalPage from './components/JournalPage.vue'
import LoginPage from './components/LoginPage.vue'
import MessagesPage from './components/MessagesPage.vue'
import SettingsPage from './components/settings-page/SettingsPage.vue'
import ModesPage from './components/ModesPage.vue'
import AddJournal from './components/AddJournal.vue'
import ajax from './axios.config.js'
import store from './store/store.js'

Vue.use(Router);

const router = new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'basePage',
            component: BasePage,
            children: [
                {
                    path: '/dashboard',
                    name: 'dashboard',
                    component: Dashboard
                },
                {
                    path: '/:plant/:journal/:shift_id',
                    name: 'defaultJournalPage',
                    component: JournalPage
                },
                {
                    path: '/messages',
                    name: 'messagesPage',
                    component: MessagesPage
                },
                {
                    path: '/addjournal',
                    name: 'addJournal',
                    component: AddJournal
                },
                {
                    path: '/settings',
                    name: 'settingsPage',
                    component: SettingsPage
                },
                {
                    path: '/modes',
                    name: 'modesPage',
                    component: ModesPage
                }
            ]
        },
        {
            path: '/login',
            name: 'loginPage',
            component: LoginPage
        }
    ]
})

router.beforeEach((to, from, next) => {
    if (!VueCookies.get('Authorization') && to.name !== 'loginPage') {
        next('/login')
    }
    else {
        console.dir(VueCookies.get('Authorization'))
        console.log(to)
        if (to.path == "/") {
            ajax.get("http://localhost:8000/api/setting?name=defaultpage", {withCredentials: true })
                .then((response) => {
                    console.log("default url", response.data.defaultPage)
                    if (response.data.defaultPage) {
                        next(response.data.defaultPage)
                        var temp = response.data.defaultPage.split("/")
                        var plantName = temp[1]
                        var journalName = temp[2]
                        var id = temp[3]
                        if (store.getters['journalState/isSynchronized']) {
                            store.dispatch('journalState/loadJournal', {
                              'plantName': plantName,
                              'journalName': journalName,
                            })
                                .then((id) => {
                                    next('/' + plantName + '/' + journalName + '/' + id)
                                    this.setActiveItem()
                                    store.dispatch('journalState/loadShifts', { plant: plantName, journal: journalName })
                                })
                        }
                    }
                })
        }
        else {
            next()
        }
    }
})

export default router
