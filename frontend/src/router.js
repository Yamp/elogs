import Vue from 'vue'
import Router from 'vue-router'
import BasePage from './components/BasePage.vue'
import JournalPage from './components/JournalPage.vue'
import LoginPage from './components/LoginPage.vue'
import MessagesPage from './components/MessagesPage.vue'
import SettingsPage from './components/SettingsPage.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'basePage',
            component: BasePage,
            children: [
                {
                    path: ':journal/:shift_id',
                    name: 'journalPage',
                    component: JournalPage
                },
                {
                    path: '/messages',
                    name: 'messagesPage',
                    component: MessagesPage
                },
                {
                    path: '/settings',
                    name: 'settingsPage',
                    component: SettingsPage
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