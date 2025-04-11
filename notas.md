# 📘 Notas.md

### ✅ **TypeScript: Tipagem adequada para todas as estruturas e funções**

- Todas as variáveis, funções e classes devem ter tipos explícitos definidos, sempre que possível.
```ts
let nome: string = "Caneta";
let preco: number = 12.5;
let disponivel: boolean = true;
```

---

### ✅ **Modularização: Boas práticas de orientação a objetos**

- Organização em arquivos e pastas por responsabilidade (`entities`, `services`, `cli`, etc).
- Separação entre lógica de negócio e interação com o usuário.
```ts
// Exemplo: separação de entidade e lógica de CRUD
// entities/Product.ts
export class Product {
  constructor(public id: number, public nome: string) {}
}

// services/ProductService.ts
import { Product } from "../entities/Product";
export class ProductService {
  private produtos: Product[] = [];
}
```

---

### ✅ **Persistência em Memória**

- Uso de arrays para simular banco de dados:
```ts
const produtos: Produto[] = [];

function adicionarProduto(produto: Produto): void {
  produtos.push(produto);
}
```

---

### ✅ **Tipos básicos e anotações de tipo**
```ts
let idade: number = 30;
let nome: string = "Maria";
let ativo: boolean = true;
let vazio: null = null;
let indefinido: undefined = undefined;
let retorno: void = undefined;
let qualquerCoisa: any = "pode ser qualquer tipo";
```

---

### ✅ **Tipos condicionais, intersection types e union types**

```ts
// Union Type
type ID = string | number;

function buscarPorId(id: ID): void {
  console.log("ID:", id);
}

// Intersection Type
type Pessoa = { nome: string };
type Funcionario = Pessoa & { cargo: string };

// Type Conditional
type Mensagem<T> = T extends string ? string : never;
```

---

### ✅ **Interfaces e tipos personalizados (`type` vs `interface`)**

```ts
// Interface
interface Categoria {
  id: number;
  nome: string;
  descricao?: string; // propriedade opcional
}

// Type
type Produto = {
  id: number;
  nome: string;
  preco: number;
};
```

> **Interface** é mais usada para objetos, enquanto `type` pode compor tipos complexos (unions, intersections).

---

### ✅ **Interfaces com propriedades opcionais**

```ts
interface Usuario {
  id: number;
  nome: string;
  email?: string; // opcional
}
```

---

### ✅ **Funções em TypeScript**

```ts
// Declaração com tipo
function soma(a: number, b: number): number {
  return a + b;
}

// Parâmetro opcional
function saudacao(nome?: string): string {
  return `Olá, ${nome ?? "visitante"}`;
}
```

---

### ✅ **Classes, Herança e Modificadores**

```ts
class Pessoa {
  constructor(public nome: string, protected idade: number) {}

  apresentar(): string {
    return `Nome: ${this.nome}, Idade: ${this.idade}`;
  }
}

class Funcionario extends Pessoa {
  private cargo: string;

  constructor(nome: string, idade: number, cargo: string) {
    super(nome, idade);
    this.cargo = cargo;
  }

  getCargo(): string {
    return this.cargo;
  }
}
```

---

### ✅ **Generics**

```ts
function identidade<T>(valor: T): T {
  return valor;
}

const numero = identidade<number>(10);
const texto = identidade<string>("Olá");
```

---

### ✅ **Enums e Mapeamento de Valores**

```ts
enum Status {
  Ativo = "ativo",
  Inativo = "inativo",
  Pendente = "pendente"
}

function verificarStatus(s: Status): void {
  console.log(`Status atual: ${s}`);
}
```

---

### ✅ **Configuração do `tsconfig.json`**

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "esModuleInterop": true,
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    "rootDir": "./src",
    "outDir": "./dist"
  }
}
```

**Comentários:**
- `"strict": true` — habilita verificação estrita de tipo.
- `"esModuleInterop": true` — permite importações de módulos CommonJS.
- `"experimentalDecorators"` e `"emitDecoratorMetadata"` — necessários para usar decorators do TypeORM.

---

### ✅ **TypeORM**

- ORM para manipular banco de dados com classes.
- Uso de `@Entity`, `@PrimaryGeneratedColumn`, `@Column`, etc.

```ts
import { Entity, Column, PrimaryGeneratedColumn } from "typeorm";

@Entity()
export class Category {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  nome: string;

  @Column({ nullable: true })
  descricao?: string;
}
```

- Relacionamentos:
```ts
@OneToMany(() => Product, product => product.categoria)
products: Product[];
```

- Conexão com banco:
```ts
import "reflect-metadata";
import { DataSource } from "typeorm";
import { Category } from "./entities/category";

export const AppDataSource = new DataSource({
  type: "sqlite",
  database: "./db.sqlite",
  synchronize: true,
  entities: [Category],
});
