<template>
  <div id="sidebar" class="widget-area col300" role="complementary">
    <div id="sidebar-wrap" class="clearfix">
      <aside id="recent-posts-2" class="widget widget_recent_entries">
        <h2 class="widget-title">Errors</h2>
        <div class="content">
          <p align="center" style="background-color: #82D51A;padding: 5px;color: white;font-weight: bold;border: solid 1px black;text-shadow: 0px 0px 3px black;">
            Show <a style="color: #FFE249;" target="_blank" href="/404">404 error</a> page！
          </p>
        </div>
      </aside>
      <aside id="recent-posts-3" class="widget widget_recent_entries">
        <h2 class="widget-title">Links</h2>
        <ul>
          <li>
            <a target="_blank" href="http://www.pythondoc.com/pythontutorial27/index.html">Python 2.7 tutorial</a>
          </li>
          <li>
            <a target="_blank" href="http://www.pythondoc.com/pythontutorial3/index.html">Python 3.3 tutorial</a>
          </li>
          <li>
            <a target="_blank" href="http://www.pythondoc.com/sphinx/index.html">sphinx</a>
          </li>
        </ul>
      </aside>
      <aside id="recent-posts-3" class="widget widget_recent_entries">
        <h2 class="widget-title">New posts</h2>
        <ul>
          <li
            v-for="post in newPosts"
            :key="`new-post-${post.postId}`"
          >
            <a
              :title="post.title"
              :href="`/article/${post.postId}`"
            >
              {{post.title}}
            </a>
          </li>
        </ul>
      </aside>
      <aside id="recent-posts-4" class="widget widget_recent_entries">
        <h2 class="widget-title">Hot posts</h2>
        <ul>
          <li
            v-for="post in hotArticles"
            :key="`hot-${post.postId}`"
          >
            <a
              :title="post.title"
              :href="`/article/${post.postId}`"
            >
              {{post.title}}
            </a>
          </li>
        </ul>
      </aside>
      <aside id="tag_cloud-5" class="widget widget_tag_cloud">
        <h2 class="widget-title">Tags</h2>
        <div class="tagcloud">
          <a
            v-for="(tag, tagId) in tags"
            :key="`tag-${tag.tagId}`"
            class="tag-link-17"
            :style="`${colorClass[tagId]}${rowClass[tagId]}`"
            :href="`/tag/${tag.tagId}`"
          >
            {{ tag.name }}
          </a>
        </div>
      </aside>
      <aside id="recent-posts-4" class="widget widget_recent_entries">
        <h2 class="widget-title">Categories</h2>
        <ul>
          <li
            v-for="category in categories"
            :key="`category-${category.categoryId}`"
          >
            <a
              :title="`Category ${category.text}`"
              :href="`/category/${category.categoryId}`"
            >
              {{ category.text }}({{ category.postsCount }})
            </a>
          </li>
        </ul>
      </aside>
      <aside id="recent-comments-3" class="widget widget_recent_comments">
        <h2 class="widget-title">Comments</h2>
        <ul id="recent-comments">
          <li
            v-for="comment in comments"
            :key="`comment-${comment.commentId}`"
          >
            <a
              :title="comment.postId"
              :href="`/article/${comment.postId}#comments`"
            >
              {{comment.authorName}}
            </a>
            : {{ comment.brief }}&hellip;
          </li>
        </ul>
      </aside>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapState,
} from 'vuex';

@Component({
  computed: {
    ...mapState(['categories']),
  },
})
export default class Sidebar extends Vue {
  newPosts = [
    {
      postId: 1,
      title: 'Title',
    },
  ];

  hotArticles = [
    {
      postId: 1,
      title: 'Title',
    },
  ];

  tags = [
    {tagId: 1, name: 'Tag1'},
    {tagId: 2, name: 'Tag2'},
    {tagId: 3, name: 'Tag3'},
    {tagId: 4, name: 'Tag4'},
    {tagId: 5, name: 'Tag5'},
  ];

  comments = [
      {commentId: 1, postId: 1, authorName: 'author', brief: '(comment.content|safe)[:30]'},
  ];

  rowClass = [
    'font-size:12.656565656pt;',
    'font-size:8pt;',
    'font-size:21.0567465745647pt;',
    'font-size:9.0567465745647pt;',
    'font-size:7.0567465745647pt;',
    'font-size:14.0567465745647pt;',
    'font-size:17.0567465745647pt;',
    'font-size:10.0567465745647pt;',
    'font-size:18.0567465745647pt;',
    'font-size:9.0567465745647pt;',
    'font-size:16.0567465745647pt;',
    'font-size:19.0567465745647pt;',
    'font-size:7.0567465745647pt;',
    'font-size:10.0567465745647pt;',
    'font-size:15.0567465745647pt;',
    'font-size:8.0567465745647pt;',
    'font-size:20.0567465745647pt;',
    'font-size:17.0567465745647pt;',
    'font-size:14.0567465745647pt;',
    'font-size:15.0567465745647pt;',
  ];

  colorClass = [
    'color:#ac1dfe;',
    'color:#bcb46e;',
    'color:#4298e7;',
    'color:#a7bce8',
    'color:#e6eca8;',
    'color:#d4349a;',
    'color:#5b48ce;',
    'color:#b5b1ea;',
    'color:#fe4516;',
    'color:#a68d32;',
    'color:#68d6e5;',
    'color:#5c8d29;',
    'color:#9c7da1;',
    'color:#243f2a;',
    'color:#6c7d99;',
    'color:#9cade9;',
    'color:#1ced29;',
    'color:#ec3de9;',
    'color:#367d29;',
    'color:#cccd29;',
  ];
}
</script>

<style>
#recent-comments a {
  display:inline !important;
  padding:0 !important;
  margin:0 !important;
}
</style>
