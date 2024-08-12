const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: '/projects', component: () => import('pages/ProjectsPage.vue') },
      { path: '/expenditures', component: () => import('pages/ExpendituresPage.vue') },
      { path: '/contractors', component: () => import('pages/ContractorsPage.vue') },
      { path: '/projects/new', component: () => import('pages/ProjectsDetailPage.vue')},
      { path: '/projects/:id(\\d+)', component: () => import('pages/ProjectsDetailPage.vue')},
      {path: '/expenditures/new', component: ()=> import('pages/ExpendituresDetailPage.vue')},
      {path: '/expenditures/:id(\\d+)', component: ()=> import('pages/ExpendituresDetailPage.vue')},
      {path: '/contractors/new', component: ()=> import('pages/ContractorsDetailPage.vue')},
      {path: '/contractors/:id(\\d+)', component: ()=> import('pages/ContractorsDetailPage.vue')},
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
