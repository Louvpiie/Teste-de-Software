# 📘 Notas.md

---

### ✅ **TypeScript: Tipagem adequada para todas as estruturas e funções**

- Todos os atributos, métodos, e variáveis têm seus tipos definidos explicitamente.
- Operadores `!` usados para indicar que variáveis obrigatórias serão inicializadas em tempo de execução (ex: `id!: string`).

```ts
@Column()
name!: string;

async createProduct(name: string, price: number, quantity: number, categoryId: string): Promise<void> { ... }
```

---

### ✅ **Modularização: Boas práticas e POO**

- Separação clara entre:
  - `entities/`: classes que representam tabelas no banco
  - `inventoryManager.ts`: classe de lógica de negócio
  - `index.ts`: interface com o usuário (CLI)
  - `data-source.ts`: configuração do banco (TypeORM)

```ts
// src/entities/Category.ts
@Entity()
export class Category {
  ...
}

// src/inventoryManager.ts
export class InventoryManager {
  ...
}
```

---

### ✅ **Persistência em Memória (Projeto 1)**

> No Projeto 2 foi utilizado banco de dados real (MySQL), mas no Projeto 1 foi usada persistência em memória com arrays:

```ts
private categories: Category[] = [];
private products: Product[] = [];
```

---

### ✅ **Tipos básicos e anotações de tipo**

```ts
let nome: string = "Produto A";
let preco: number = 29.99;
let disponivel: boolean = true;
let semValor: null = null;
let indefinido: undefined = undefined;
let retorno: void = undefined;
let qualquerCoisa: any = "Texto ou número";
```

---

### ✅ **Tipos condicionais, intersection types e union types**

```ts
// Union type
type ID = string | number;

function buscarCategoria(id: ID): void {
  ...
}

// Intersection
type Timestamps = { createdAt: Date } & { updatedAt: Date };
```

---

### ✅ **Interfaces e tipos personalizados (`type` vs `interface`)**

> Interfaces foram utilizadas no Projeto 1 (persistência em memória). No Projeto 2, as entidades são definidas com classes.

```ts
interface Produto {
  id: string;
  nome: string;
  preco: number;
  descricao?: string;
}
```

---

### ✅ **Interfaces com propriedades opcionais**

```ts
interface Categoria {
  id: string;
  nome: string;
  descricao?: string;
}
```

---

### ✅ **Funções em TypeScript**

```ts
function calcularDesconto(preco: number, percentual?: number): number {
  return percentual ? preco * (1 - percentual / 100) : preco;
}
```

---

### ✅ **Classes, Herança e modificadores de acesso**

```ts
class Pessoa {
  constructor(public nome: string, private idade: number) {}

  apresentar(): string {
    return `${this.nome}, ${this.idade} anos`;
  }
}
```

- `public`: acessível em qualquer lugar
- `private`: acessível apenas dentro da classe
- `protected`: acessível na classe e subclasses

---

### ✅ **Generics**

```ts
function identity<T>(valor: T): T {
  return valor;
}

const numero = identity<number>(42);
const texto = identity<string>("Exemplo");
```

---

### ✅ **Enums e Mapeamento de Valores**

```ts
enum StatusProduto {
  Ativo = "ativo",
  Inativo = "inativo",
}

function exibirStatus(status: StatusProduto): void {
  console.log(`Status: ${status}`);
}
```

---

### ✅ **Configuração `tsconfig.json` (com comentários)**

```json
{
  "compilerOptions": {
    "target": "ES2020",                      // Compilação moderna
    "module": "commonjs",                   // Compatibilidade com Node.js
    "strict": true,                         // Habilita verificação estrita
    "esModuleInterop": true,                // Importação de módulos CommonJS
    "experimentalDecorators": true,         // Suporte a decorators (@Entity, etc)
    "emitDecoratorMetadata": true,          // Emissão de metadados para decorators
    "rootDir": "./src",
    "outDir": "./dist"
  }
}
```

---

### ✅ **TypeORM**

- ORM utilizado para mapear classes em tabelas no banco de dados (MySQL).
- Mapeamento de entidades com decorators (`@Entity`, `@Column`, `@ManyToOne`, etc).
- Relacionamentos estabelecidos entre `Category` e `Product`.

```ts
@Entity()
export class Product {
  @PrimaryGeneratedColumn("uuid")
  id!: string;

  @ManyToOne(() => Category, category => category.products)
  category!: Category;
}
```

- Conexão com o banco:
```ts
export const AppDataSource = new DataSource({
  type: 'mysql',
  host: 'localhost',
  port: 3306,
  username: 'root',
  password: 'c@tolic@',
  database: 'inventory_db',
  entities: [Category, Product],
  synchronize: true,
  logging: false,
});
```

---

### 🧠 **Observações & Boas Práticas**

- Uso de `cli-table3` para formatação de saída em tabela.
- Validação de existência da categoria antes de criar produto.
- Remoção de categoria não verifica se há produtos associados (⚠️ ponto a melhorar).
- Classes com inicialização de repositórios via `AppDataSource.getRepository()`.

---

### Integrantes

- João Filipe Alves de Albuquerque Silva UC24101
- Guilherme Souza Rocha UC24101057
- Louie Nery Silva UC24101358
- Matheus Henrique Lacerda Lopes UC24101
