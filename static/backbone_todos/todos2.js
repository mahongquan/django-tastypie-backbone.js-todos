$(function(){
  Todo = Backbone.Model.extend({
    defaults: function() {
      return {
        title: "empty todo...",
      };
    }
  });
  TodoList = Backbone.Collection.extend({
    model: Todo,
    localStorage: new Backbone.LocalStorage("todos-backbone"),
  });
  Todos = new TodoList;
  TodoView = Backbone.View.extend({
    tagName:  "li",
    template: _.template($('#item-template').html()),
    events: {
      "dblclick .view"  : "edit",
      "click a.destroy" : "clear",
      "keypress .edit"  : "updateOnEnter",
      "blur .edit"      : "close"
    },
    initialize: function() {
      this.listenTo(this.model, 'change', this.render);
      this.listenTo(this.model, 'destroy', this.remove);
    },
    render: function() {
      this.$el.html(this.template(this.model.toJSON()));
      this.input = this.$('.edit');
      return this;
    },
    edit: function() {
      this.$el.addClass("editing");
      this.input.focus();
    },
    close: function() {
      var value = this.input.val();
      if (!value) {
        this.clear();
      } else {
        this.model.save({title: value});
        this.$el.removeClass("editing");
      }
    },
    updateOnEnter: function(e) {
      if (e.keyCode == 13) this.close();
    },
    clear: function() {
      this.model.destroy();
    }
  });
  AppView = Backbone.View.extend({
    el: $("#todoapp"),
    events: {
      "keypress #new-todo":  "createOnEnter",
    },
    initialize: function() {
      this.input = this.$("#new-todo");
      this.listenTo(Todos, 'add', this.addOne);
      this.listenTo(Todos, 'reset', this.addAll);
      this.listenTo(Todos, 'all', this.render);
      this.main = $('#main');
      Todos.fetch();
    },
    render: function() {
      if (Todos.length) {
        this.main.show();
      } else {
        this.main.hide();
      }
    },
    addOne: function(todo) {
      var view = new TodoView({model: todo});
      this.$("#todo-list").append(view.render().el);
    },
    addAll: function() {
      Todos.each(this.addOne, this);
    },
    createOnEnter: function(e) {
      if (e.keyCode != 13) return;
      if (!this.input.val()) return;
      Todos.create({title: this.input.val()});
      this.input.val('');
    }
  });
  App = new AppView;
});
