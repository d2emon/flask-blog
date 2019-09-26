<template>
  <v-content id="content">
    <div class="clearfix content">
      <div id="main" class="col620 clearfix" role="main">
        block content
      </div>

      <div id="sidebar" class="widget-area col300" role="complementary">
        <div id="sidebar-wrap" class="clearfix">
          include __side.pug
        </div>
      </div>
    </div>

    <router-view />
  </v-content>
</template>
