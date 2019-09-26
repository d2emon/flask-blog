<template>
  <header id="branding" role="banner">
    <div id="inner-header" class="clearfix">
      <hgroup id="site-heading">
        <h1 id="site-title">
          <a rel="home" title="Home" href="/">Flask-Blog</a>
        </h1>
        <h2 id="site-description">My Flask-based blog.</h2>
      </hgroup>
      <nav id="access" role="navigation">
        <h1 class="assistive-text section-heading">Main menu</h1>
        <div class="skip-link screen-reader-text">
          <a title="Skip to content" href="#content">Skip to content</a>
        </div>

        <slot />
        include __head.pug
      </nav>
    </div>
  </header>
</template>
