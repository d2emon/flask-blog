<template>
  <v-container
    grid-list-xl
  >
    <v-layout wrap>
      <v-flex xs12>
        <slot />
      </v-flex>

      <feed-card
        v-for="article in articles"
        :key="article.title"
        :size="article.layout"
        :value="article"
      ></feed-card>
    </v-layout>

    <v-layout align-center>
      <v-flex xs3>
        <social-button
          v-if="page !== 1"
          class="ml-0"
          title="Previous page"
          square
          @click="fetchPage(page - 1)"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </social-button>
      </v-flex>

      <v-flex
        xs6
        text-center
        subtitle-1
      >
        PAGE {{ page }} OF {{ pages }}
      </v-flex>

      <v-flex
        xs3
        text-right
      >
        <social-button
          v-if="pages > 1 && page < pages"
          class="ml-0"
          title="Next page"
          square
          @click="fetchPage(page + 1)"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </social-button>
      </v-flex>
    </v-layout>

    <!-- Articles -->
    <article
      v-for="article in articles"
      id="post-71"
      class="post-71 post type-post status-publish format-standard hentry category-9 tag-10 tag-11 tag-12 tag-13"
    >
      <header class="entry-header">
        <h1 class="entry-title">
          <a
            rel="bookmark"
            :title="`Permalink to ${article.title}`"
            href="`/article/${article.articleId}`"
          >
            {{article.title}}
          </a>
        </h1>
        <div class="entry-meta">
          <span class="sep">Posted on </span>
          <a
            rel="bookmark"
            :title="article.title"
            :href="`/article/${article.articleId}`"
          >
            <time
              class="entry-date"
              datetime="2013-01-01T00:00:00+00:00"
            >
              {{article.createdAt}}
            </time>
          </a>

          <span class="byline">
            <span class="sep"> by </span>
            <span class="author vcard">
              <a
                class="url fn n"
                rel="author"
                :title="`View all posts by ${article.author}`"
                href="/"
              >
                {{article.author}}
              </a>
            </span>
          </span>

          <span
            class="sep"
            style="float:right"
          >
            <p>
              <a
                class="more"
                :href="`/article/${article.articleId}`"
              >
                &raquo;
              </a>
            </p>
          </span>

          <span
            class="sep"
            style="float:right"
          >
            <a
              :title="`Comments for ${article.title}`"
              :href="`/article/${article.articleId}#comments`"
            >
              {{article.commentsCount}} comments
            </a>
          </span>

          <span
            class="sep"
            style="float:right"
          >
            {{ article.views }} views
          </span>
        </div>
      </header>
      <div class="entry-content post_content">
        <!-- { (a.content|safe|html2textile)[:3000] }} &hellip; -->
        <template v-html="article.content"></template>
        <template v-if="article.content && article.content.length > 3000"> &hellip</template>
        <p>
          <a
            class="more"
            :href="`/article/${article.articleId}`"
            style="float:right"
          >
            &raquo;
          </a>
        </p>
      </div>
      <footer class="entry-meta">
        <span class="cat-links">
          Posted in
          <a
            rel="tag"
            :title="`Category ${article.category}`"
            :href="`/category/${article.categoryId}`"
          >
            {{article.category}}
          </a>
        </span>
        <span class="sep">|</span>
        <span class="tag-links">
          Tagged:
          <span
            v-for="(tag, tagId) in article.tags"
            :key="`tag-${tagId}`"
          >
            <a
              rel="tag"
              :href="`/tag/${tag.tagId}`"
            >
              {{tag.name}}
            </a>
          </span>
        </span>
      </footer>
    </article>

    <!-- Pagination -->
    <div
      id="Pagination"
      class="pagination"
      v-if="pages > 1"
    >
      <a
        @click="fetchPage(1)"
      >
        &laquo;
      </a>
      <span
        v-for="pageId in pages"
        :key="`page-${pageId}`"
      >
        <template v-if="pageId">
          <span
            v-if="pageId === page"
            class="current"
          >
            {{pageId}}
          </span>
          <a
            v-else
            @click="fetchPage(pageId)"
          >
            {{pageId}}
          </a>
        </template>
        <span
          v-else
          class="ellipsis"
        >
          …
        </span>
      </span>
      <a
        @click="fetchPage(page + 1)"
      >
        &raquo;
      </a>
    </div>
    <!--
      | Commented
      | {% set items=articles %}
      ul(class="pagination pagination-sm", style="display:inherit;")
        li(class="{% if not items.has_prev %}disabled{% endif %}")
          a(href="?page={ items.prev_num }}")
            span(class="glyphicon glyphicon-menu-left")
        | {%- for page in items.iter_pages() %}
        | {% if page %}
        li(class="{% if page == items.page %}active{% endif %}")
          a(href="?page={ page }}") { page }}
        | {% else %}
        li
          span(class=ellipsis) …
        | {% endif %}
        | {%- endfor %}
        li(class="{% if not items.has_next %}disabled{% endif %}")
          a(href="?page={ items.next_num }}")
            span(class="glyphicon glyphicon-menu-right")
    -->
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import {
  mapActions,
  mapGetters,
  mapState,
} from 'vuex';

export default Vue.extend({
  components: {
    SocialButton: () => import('@/components/controls/SocialButton.vue'),
    FeedCard: () => import('@/components/FeedCard.vue'),
  },
  computed: {
    ...mapState([
      'articles',
      'page',
    ]),
    ...mapGetters([
      'pages',
    ]),
  },
  methods: {
    ...mapActions(['fetchPage']),
  },
  watch: {
    page() {
      window.scrollTo(0, 0);
    },
  },
})
</script>
