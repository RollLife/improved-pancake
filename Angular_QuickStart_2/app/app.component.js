"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var AppComponent = (function () {
    function AppComponent() {
        this.title = 'Angular JS version 2 test site';
        this.person = {
            id: 1,
            name: 'demian',
            webpage: 'http://localhost:3000'
        };
    }
    AppComponent = __decorate([
        core_1.Component({
            selector: 'my-app',
            template: "\n\t<h1>{{title}}</h1>\n\t<h2>I'm {{person.name}}</h2>\n\t<div>My Website : <a href={{person.webpage}}>{{person.webpage}}</a></div>\n\t<div>\n\t\t<label>name : </label>\n\t\t<div><input [(ngModel)]=\"person.name\" placeholder=\"name\"></div><br>\n\t\t<label>webpage: </label>\n\t\t<div><input [(ngModel)]=\"person.webpage\" placeholder=\"webpage\"></div>\n\t</div>\n\t"
        }), 
        __metadata('design:paramtypes', [])
    ], AppComponent);
    return AppComponent;
}());
exports.AppComponent = AppComponent;
//지금까지 안됬던 이유는 app.module.ts 에서 Forms module 부분을 넣지 않았기에 실행이 되지 않았다. 
//# sourceMappingURL=app.component.js.map