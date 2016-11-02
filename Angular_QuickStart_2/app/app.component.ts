import { Component } from '@angular/core';

interface Person {
	id : number;
	name: string;
	webpage : string;
}

@Component({
	selector: 'my-app',
	template: `
	<h1>{{title}}</h1>
	<h2>I'm {{person.name}}</h2>
	<div>My Website : <a href={{person.webpage}}>{{person.webpage}}</a></div>
	<div>
		<label>name : </label>
		<div><input [(ngModel)]="person.name" placeholder="name"></div><br>
		<label>webpage: </label>
		<div><input [(ngModel)]="person.webpage" placeholder="webpage"></div>
	</div>
	`
})

export class AppComponent {
	title = 'Angular JS version 2 test site';
	person: Person = {
		id : 1,
		name : 'demian',
		webpage: 'http://localhost:3000'
	};
}

//지금까지 안됬던 이유는 app.module.ts 에서 Forms module 부분을 넣지 않았기에 실행이 되지 않았다.