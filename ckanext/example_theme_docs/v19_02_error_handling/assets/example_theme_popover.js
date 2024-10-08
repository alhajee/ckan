"use strict";

ckan.module("example_theme_popover", function ($) {
  return {
    initialize: function () {
      $.proxyAll(this, /_on/);
      this.el.popover({
        title: this.options.title,
        html: true,
        content: this._("Loading..."),
        placement: "left",
      });
      this.el.on("click", this._onClick);
    },

    _snippetReceived: false,

    _onClick: function (event) {
      if (!this._snippetReceived) {
        this.sandbox.client.getTemplate(
          "foobar.html",
          this.options,
          this._onReceiveSnippet,
          this._onReceiveSnippetError
        );
      }
    },

    _onReceiveSnippet: function (html) {
      this.el.popover("destroy");
      this.el.popover({
        title: this.options.title,
        html: true,
        content: html,
        placement: "left",
      });
      this.el.popover("show");
      this._snippetReceived = true;
    },

    // This function is called when FMLD responds with an error.
    _onReceiveSnippetError: function (error) {
      this.el.popover("destroy");

      var content = error.status + " " + error.statusText + " :(";
      this.el.popover({
        title: this.options.title,
        html: true,
        content: content,
        placement: "left",
      });

      this.el.popover("show");
      this._snippetReceived = true;
    },
    // End of _onReceiveSnippetError
  };
});
