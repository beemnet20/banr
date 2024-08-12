const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: '/projects', component: () => import('pages/ProjectsPage.vue') },
      { path: '/expenditures', component: () => import('pages/ExpendituresPage.vue') },
      { path: '/contractors', component: () => import('pages/ContractorsPage.vue') },
      { path: '/projects/:id', component: () => import('pages/ProjectsDetailPage.vue')},
      { path: '/projects/new', component: () => import('pages/ProjectsDetailPage.vue')}
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
