document.addEventListener('DOMContentLoaded', () => {
    // Referências aos botões de navegação e visualizações
    const btnQuemSouDesktop = document.getElementById('btn-sidebar-quem-sou'); // Este talvez não exista mais dependendo do HTML final
    const btnBlogDesktop = document.getElementById('btn-sidebar-blog');     // Este talvez não exista mais dependendo do HTML final

    const btnQuemSouMobile = document.getElementById('btn-sidebar-quem-sou-mobile');
    const btnBlogMobile = document.getElementById('btn-sidebar-blog-mobile');
    
    const btnLerBlogQuemSou = document.getElementById('btn-ler-blog-quem-sou');

    const quemSouView = document.getElementById('quem-sou-view');
    const blogView = document.getElementById('blog-view');

    // Função para mostrar uma view e ocultar a outra
    const showView = (viewToShow, viewToHide) => {
        viewToShow.classList.remove('hidden');
        viewToHide.classList.add('hidden');
    };

    // Função para atualizar o estado ativo dos botões
    const updateButtonState = (activeBtnDesktop, inactiveBtnDesktop, activeBtnMobile, inactiveBtnMobile) => {
        if (btnQuemSouDesktop) { // Verifica se o botão desktop existe
            btnQuemSouDesktop.classList.remove('active');
            btnBlogDesktop.classList.remove('active');
            if (activeBtnDesktop) activeBtnDesktop.classList.add('active');
        }

        if (btnQuemSouMobile) { // Verifica se o botão mobile existe
            btnQuemSouMobile.classList.remove('active');
            btnBlogMobile.classList.remove('active');
            if (activeBtnMobile) activeBtnMobile.classList.add('active');
        }
    };

    // Event Listeners para botões (Desktop - se existirem)
    if (btnQuemSouDesktop) {
        btnQuemSouDesktop.addEventListener('click', () => {
            showView(quemSouView, blogView);
            updateButtonState(btnQuemSouDesktop, btnBlogDesktop, btnQuemSouMobile, btnBlogMobile);
        });
    }

    if (btnBlogDesktop) {
        btnBlogDesktop.addEventListener('click', () => {
            showView(blogView, quemSouView);
            updateButtonState(btnBlogDesktop, btnQuemSouDesktop, btnBlogMobile, btnQuemSouMobile);
        });
    }

    // Event Listeners para botões (Mobile)
    if (btnQuemSouMobile) {
        btnQuemSouMobile.addEventListener('click', () => {
            showView(quemSouView, blogView);
            updateButtonState(null, null, btnQuemSouMobile, btnBlogMobile); // Passa null para desktop, pois não existem
        });
    }

    if (btnBlogMobile) {
        btnBlogMobile.addEventListener('click', () => {
            showView(blogView, quemSouView);
            updateButtonState(null, null, btnBlogMobile, btnQuemSouMobile); // Passa null para desktop, pois não existem
        });
    }

    // Event Listener para o botão "Ler o Blog" na seção "Quem sou"
    if (btnLerBlogQuemSou) {
        btnLerBlogQuemSou.addEventListener('click', (e) => {
            e.preventDefault(); // Impede o comportamento padrão do link
            showView(blogView, quemSouView);
            updateButtonState(btnBlogDesktop, btnQuemSouDesktop, btnBlogMobile, btnQuemSouMobile); // Ativa o botão Blog
        });
    }

    // Garante que a view "Quem sou" seja exibida por padrão ao carregar
    showView(quemSouView, blogView);
    updateButtonState(btnQuemSouDesktop, btnBlogDesktop, btnQuemSouMobile, btnBlogMobile);
});

document.addEventListener('DOMContentLoaded', () => {
    // 1. Seleciona todos os botões de filtro e todos os cards de postagem
    const filtroBotoes = document.querySelectorAll('.btn-filtro');
    const postCards = document.querySelectorAll('.post-card');

    // 2. Adiciona o ouvinte de evento a cada botão
    filtroBotoes.forEach(button => {
        button.addEventListener('click', () => {
            
            // a) Remove a classe 'ativo' de todos os botões e adiciona ao clicado
            filtroBotoes.forEach(btn => btn.classList.remove('ativo'));
            button.classList.add('ativo');

            // b) Pega a categoria desejada do atributo data-categoria
            const categoria = button.getAttribute('data-categoria');

            // 3. Itera sobre os cards para filtrar
            postCards.forEach(card => {
                const cardCategoria = card.getAttribute('data-categoria');

                // 4. Lógica de mostrar/esconder
                if (categoria === 'todos' || cardCategoria === categoria) {
                    // Se for 'todos' OU a categoria do card bater com a clicada:
                    card.classList.remove('hidden'); // 'hidden' é a classe que oculta no CSS
                } else {
                    // Esconde todos os outros
                    card.classList.add('hidden');
                }
            });
        });
    });
});