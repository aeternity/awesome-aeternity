# Awesome Æternity [![awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
    <img src="logo.svg" height="40">
</p>

The æternity blockchain is an Erlang-based scalable smart contract platform engineered by programming pioneers to address some of the most fundamental challenges native to earlier blockchains. By redesigning blockchain technology at the protocol level, the æternity developer community has enabled the core protocol to understand and integrate a rich set of functionalities out of the box.

## Contents

- [News and Updates](#news-and-updates)
- [Community](#community)
  - [æUnited](#æunited)
  - [Bounties](#bounties)
  - [Grants](#grants)
  - [Initiatives](#initiatives)
- [Whitepaper](#whitepaper)
- [Protocol](#protocol)
- [Infrastructure & core components](#infrastructure--core-components)
  - [Node and Middleware](#node-and-middleware)
  - [Virtual Machine](#virtual-machine)
- [Official Hosted Services](#official-hosted-services)
  - [Http compiler](#http-compiler)
  - [Node & middleware](#node--middleware)
- [Explorers](#explorers)
  - [Mainnet](#mainnet)
  - [Testnet](#testnet)
- [Faucets](#faucets)
- [Wallets](#wallets)
  - [Browser extensions](#browser-extensions)
  - [Cloud & custodial wallets](#cloud--custodial-wallets)
  - [Hardware wallets](#hardware-wallets)
  - [Mobile wallets](#mobile-wallets)
- [Development](#development)
  - [Software Development Kits (SDKs)](#software-development-kits-sdks)
  - [Smart Contract Development (Sophia language)](#smart-contract-development-sophia-language)
  - [CLIs, other Plugins & Libraries](#clis-other-plugins--libraries)
  - [Examples & Code-Snippets](#examples--code-snippets)
  - [Hackathons](#hackathons)
- [Decentralized Applications (æpps)](#decentralized-applications-æpps)
- [Education](#education)
  - [Courses](#courses)
  - [Documentation](#documentation)
  - [Videos](#videos)
- [Exchanges](#exchanges)

## News and Updates
- https://blog.aeternity.com/ - The æternity blog.
- https://twitter.com/aeternity - Official Twitter account.
- https://twitter.com/aeternityTECH - Tech updates.
    - Currently not actively managed
- https://forum.aeternity.com/c/announcements/18 - General news and announcements.
- https://forum.aeternity.com/c/announcements/development-news-and-updates/35 - Core Dev Updates.

## Community
For questions & discussions check out the official [Forum](https://forum.aeternity.com).

Other places to get in touch:

- [Discord](https://discord.gg/Htq9YdHyT4)
- Telegram
    - [æternity](https://t.me/joinchat/QHJopU1Xol0qptG8) - Official English channel.
    - [æternity [RU]](https://t.me/aeternityRU) - Official Russian channel.
    - [æternity Español](https://t.me/aeternityEsp) - Official Spanish channel.
    - [Superhero](https://t.me/superherocom) - Official channel to discuss Superhero.
    - [AE中国社区(Wetrue)](https://t.me/AEChinaCommunity) - Community maintained Chinese channel.
    - [æternity trading](https://t.me/aeternitytrading) - Community maintained channel for trading discussions.
- [Reddit](https://www.reddit.com/r/Aeternity)
- [YouTube](https://www.youtube.com/channel/UCEsM0b7QPazeMR80DxNkzCA)
- [LinkedIn](https://www.linkedin.com/company/aeternity/)

### æUnited
- https://blog.aeternity.com/launching-the-future-of-open-source-collaboration-bc677a4049ff
- https://forum.aeternity.com/tag/ae-united

### Bounties
- https://github.com/aeternity/bounties

### Grants
- https://www.aeternity-foundation.org
- https://forum.aeternity.com/c/li-foundation/grant/

### Initiatives
- [AEChina](https://www.aechina.io) - News & updates for the Chinese community.
- [AEkiti](https://aekiti.com) - Community of developers in Ekiti.
    - https://aekiti.medium.com/
    - https://github.com/aekiti/devstudyjaem-ekiti
- [Jæm sessions](https://forum.aeternity.com/t/introducing-jaem-sessions/9554) - Regular virtual developer meetings.

## Whitepaper
- [2017 Whitepaper](https://blockchainlab.com/pdf/%91ternity-blockchain-whitepaper.pdf) - The original whitepaper.
    - Repository: https://github.com/aeternity/whitepaper
- [2020 Whitepaper](https://github.com/keypair/white-paper/blob/master/aeternity-whitepaper.pdf) - Draft that reflects the current state.
    - Repository: https://github.com/aeternity/white-paper

## Protocol
The specification of the æternity protocol can be found here:

- https://aeternity.com/protocol

For off-protocol standard proposals check out the AEXpansions:

- https://github.com/aeternity/AEXs

## Infrastructure & core components

### Node and Middleware
- [æternity](https://github.com/aeternity/aeternity) - The official æternity node written in Erlang.
    - Documentation: https://docs.aeternity.io
    - API Documentation: https://api-docs.aeternity.io
- [ae_mdw](https://github.com/aeternity/ae_mdw) - The official æternity middleware written in Elixir.
    - Uses a plugin architecture where the node itself serves as extension to the middleware.

**Note**

- You can download the latest release as well as backups for mainnet or testnet here: https://downloads.aeternity.io
- For the middleware currently no snapshots exists and a full sync is required.

Community developed middleware:
- [aepp-middleware-mn](https://github.com/kryztoval/aepp-middleware-mn) - Middleware implementation written in Node.js.

### Virtual Machine
- [aebytecode](https://github.com/aeternity/aebytecode) - Library and stand alone assembler for æternity bytecode.

## Official Hosted Services

### Http compiler
- https://compiler.aeternity.io/version

### Node & middleware
###### Mainnet
- https://mainnet.aeternity.io/v3/status - The status endpoint of the Node API.
- https://mainnet.aeternity.io/mdw/status - The status endpoint of the Middleware API.

###### Testnet
- https://testnet.aeternity.io/v3/status - The status endpoint of the Node API.
- https://testnet.aeternity.io/mdw/status - The status endpoint of the Middleware API.

**Note**

- Everybody is encouraged to host their own infrastructure
    - https://blog.aeternity.com/why-run-an-ae-node-and-how-to-do-it-8b95a685f683
- You should ***never*** rely on the hosted infrastructure of æternity for applications running in production!

## Explorers

### Mainnet
- [AEknow](https://aeknow.org) - Explorer that also shows mining stats developed by the community.
    - https://github.com/jdgcs/aeknow
- [aenalytics](https://aenalytics.org) - Explorer with focus on UX and the æternity naming system (AENS).
- [æternity explorer](https://explorer.aeternity.io) - Default explorer provided by æternity.
    - https://github.com/aeternity/mdw-frontend
- https://ae.criesca.net:3011/explorer/dashboard.html
    - https://github.com/kryztoval/aepp-middleware-mn/tree/master/explorer

### Testnet
- [aenalytics](https://testnet.aenalytics.org) - Explorer with focus on UX and the æternity naming system (AENS).
- [æternity explorer](https://explorer.testnet.aeternity.io) - Default explorer provided by æternity.

## Faucets
- [aepp-faucet](https://faucet.aepps.com) - Get AE tokens to play around on testnet.
    - https://github.com/aeternity/aepp-faucet-nodejs

## Wallets

### Browser extensions
- Superhero Wallet - The most advanced æternity wallet with additional features for Superhero.com.
    - [Brave / Chrome](https://chrome.google.com/webstore/detail/superhero/mnhmmkepfddpifjkamaligfeemcbhdne?hl=en)
    - [Firefox](https://addons.mozilla.org/en-US/firefox/addon/superhero-wallet/)
- [Waellet](https://github.com/waellet/waellet) - Currently not actively developed.

### Cloud & custodial wallets
- [Venly](https://www.venly.io/) - User friendly & (optionally) recoverable cloud wallet. Formerly known as *ArkaneWallet*.
    - https://medium.com/arkane-network/we-welcome-aeternity-a3f5ea33455d
    - https://www.youtube.com/watch?v=VL22PDeCQUQ

### Hardware wallets
- [Ledger](https://ledger.com) - Support is available via web interface of the [Base aepp](https://base.aepps.com).

### Mobile wallets
- [AirGap](https://airgap.it) - Cryptocurrency hardware wallet based on a two device approach, increasing security and usability with YOU in the driver's seat.
    - [AirGap Wallet](https://github.com/airgap-it/airgap-wallet) - Installed on an everyday smartphone. This app has only access to public information.
        - [Android / APK](https://github.com/airgap-it/airgap-wallet/releases)
        - [Android / Store](https://play.google.com/store/apps/details?id=it.airgap.wallet)
        - [iOS](https://apps.apple.com/app/airgap-wallet/id1420996542#?platform=iphone)
    - [AirGap Vault](https://github.com/airgap-it/airgap-vault) - Installed on a smartphone that has no connection to any network, thus it is air gapped. This app handles the private key.
        - [Android / APK](https://github.com/airgap-it/airgap-vault/releases)
        - [Android / Store](https://play.google.com/store/apps/details?id=it.airgap.vault)
        - [iOS](https://apps.apple.com/app/airgap-vault-secure-secrets/id1417126841#?platform=iphone)
- [Atomic Wallet](https://atomicwallet.io/aeternity-wallet) - Wallet that supports many different cryptocurrencies.
    - [Android / APK](https://get.atomicwallet.io/download/atomicwallet.apk)
    - [Android / Store](https://play.google.com/store/apps/details?id=io.atomicwallet)
    - [iOS](https://apps.apple.com/app/atomic-wallet/id1478257827)
- [Base aepp](https://github.com/aeternity/aepp-base) - Mobile wallet with possibility to establish a remote connection to the web application.
    - [Android / APK](https://github.com/aeternity/aepp-base/releases)
    - [Android / Store](https://play.google.com/store/apps/details?id=com.aeternity.base)
    - [iOS](https://apps.apple.com/us/app/base-%C3%A6pp-wallet/id1458655724#?platform=iphone)
- [Box aepp](https://github.com/sunbx/Box-aepp-mobile)
    - [Android / APK](https://www.aebox.io/) - Available by clicking the button on the official website.
    - [iOS](https://apps.apple.com/app/box-aepp/id1563610905)
- [Trust Wallet](https://github.com/trustwallet/wallet-core) - Wallet that supports many different cryptocurrencies.
    - [Android / APK](https://trustwallet.com/dl/apk)
    - [Android / Store](https://play.google.com/store/apps/details?id=com.wallet.crypto.trustapp)
    - [iOS](https://apps.apple.com/app/apple-store/id1288339409#?platform=iphone)
- [Superhero Wallet](https://github.com/aeternity/superhero-wallet) - The most advanced æternity wallet with additional features for Superhero.com.
    - [Android / APK](https://github.com/aeternity/superhero-wallet/releases)
    - [Android / Store](https://play.google.com/store/apps/details?id=com.superhero.cordova)
    - [iOS](https://apps.apple.com/ro/app/superhero-wallet/id1502786641)

**Note**

- Base æpp is currently the only wallet that has support for Ledger hardware wallet
- The creation of subaccounts is currently also only available via Base æpp
    - It's also possible to derive subaccounts in advanced mode using AirGap

## Development

### Software Development Kits (SDKs)

###### Official, maintained
- [aepp-sdk-js](https://github.com/aeternity/aepp-sdk-js)
    - Documentation: https://aeternity.com/aepp-sdk-js

###### Official, but support (currently) discontinued
- [aepp-sdk-elixir](https://github.com/aeternity/aepp-sdk-elixir) - Outdated.
    - Documentation: https://aeternity.com/aepp-sdk-elixir
- [aepp-sdk-go](https://github.com/aeternity/aepp-sdk-go) - Iris compatible, some features (e.g. `PayingForTx`) missing.
- [aepp-sdk-python](https://github.com/aeternity/aepp-sdk-python) - Outdated, can still be used for regular `SpendTx`.
    - Documentation: https://aepp-sdk-python.readthedocs.io

###### Community
- [aepp-sdk-java](https://github.com/kryptokrauts/aepp-sdk-java) - Currently outdated, full Iris compatibility coming with v3.0.0.
- [aepp-sdk-net](https://github.com/block-m3/aepp-sdk-net) - Outdated.

### Smart Contract Development (Sophia language)

###### Compiler
- [aesophia](https://github.com/aeternity/aesophia) - Stand alone compiler for the Sophia smart contract language.
    - Documentation: https://aeternity.com/aesophia
- [aesophia_cli](https://github.com/aeternity/aesophia_cli) - The command line client for the Sophia compiler.
- [aesophia_http](https://github.com/aeternity/aesophia_http) - The http interface to the Sophia compiler.

###### REPL (read–eval–print loop)
- [REPL](https://repl.aeternity.io) - Access to the hosted web application.
- [aerepl](https://github.com/aeternity/aerepl) - A read–eval–print loop (REPL) Sophia in an interactive way.
- [aerepl_http](https://github.com/aeternity/aerepl_http) - A simple web application which provides an interface to aerepl.

###### Frameworks
- [aepp-aeproject-js](https://github.com/aeternity/aepp-aeproject-js) - A CLI tool for local Smart Contract development & testing.
    - requires a [Docker](https://www.docker.com/) installation to run the local stack (node + http compiler)
- [AEasy](https://aeasy.io) - Development framework built by the community.

###### IDEs & Plugins
- [AEstudio](https://studio.aepps.com/) - A web IDE for rapid prototyping (formerly known as *Fire Editor*).
    - https://github.com/aeternity/fire-editor
- Language Server Protocol
    - https://forum.aeternity.com/t/aesophia-vscode-a-sophia-vscode-extension-with-basic-lsp-implementation/7572
- Syntax Highlighting
    - Notepad++:
        - https://github.com/aeternity/tutorials/blob/master/sophia-language-definition-for-notepad++.md
    - VIM
        - https://forum.aeternity.com/t/introducing-sophia-syntax-extension-for-vim-text-editor/9250/3
    - VSCode:
        - https://medium.com/hack/aeternity-sophia-language-visual-studio-code-extension-a326258fb399

###### Smart Contract Standards
- [æternity fungible token](https://github.com/mradkov/aeternity-fungible-token) - The reference implementation of the AEX-9 standard.
- æternity NFT
    - WIP, see https://forum.aeternity.com/t/aeternity-nft-token-standard/9781

###### Starters / Boilerplates (Full-stack)
- [aepp-boilerplate-vue](https://github.com/aeternity/aepp-boilerplate-vue) - Provides a build pipeline, wallet discovery (AEX-2) & styled components.

### CLIs, other Plugins & Libraries
- [aepp-calldata-js](https://github.com/aeternity/aepp-calldata-js) - Library to enable client-side encoding/decoding.
- [aepp-cli-js](https://github.com/aeternity/aepp-cli-js) - A command line interface for the æternity blockchain.
- [app-aeternity](https://github.com/LedgerHQ/app-aeternity) - Wallet application framework for Ledger.
- [contraect-maven-plugin](https://github.com/kryptokrauts/contraect-maven-plugin) - A plugin to generate Java classes to easily interact with Smart Contracts on the JVM.
- [hd-wallet-js](https://github.com/aeternity/hd-wallet-js) - HD wallet library.

**Note**

- The tools for Smart Contract interactions currently rely on the http compiler of Sophia for compiling contracts as well as encoding/decoding of calldata.
- æternity is aiming to solve that problem by providing a way to transpile Erlang to PureScript
    - https://blog.aeternity.com/erlscripten-92c815786987
    - https://github.com/erlscripten

### Examples & Code-Snippets

###### AENS
- [4evaAens](https://github.com/u2467/4evaAens) - Auto bidding for AENS (JavaScript) / Hack&Play 11.2019.
- [forever_aens](https://github.com/DanielaIvanova/forever_aens) - Auto bidding for AENS (Elixir) / Hack&Play 11.2019.
- [name_marketplace](https://github.com/DanielaIvanova/name_marketplace) - Simple marketplace for AENS (Elixir) / Hack&Play 11.2019.
- [aens_marketplace](https://github.com/u2467/aens-marketplace) - Simple marketplace for AENS (Python) / Hack&Play 11.2019.
- [aens-name-claimer](https://github.com/kryptokrauts/aens-name-claimer) - Auto bidding for AENS (Java).

###### Oracles
- [ae-oracle-pricefeed](https://github.com/aeternity/ae-oracle-pricefeed) - A simple pricefeed oracle.
- [aeternity-simple-oracle](https://github.com/aeternity/aeternity-simple-oracle) - A simple oracle to provide weather data.
- [tipping-oracle-service](https://github.com/aeternity/tipping-oracle-service) - Tipping oracle used in Superhero (aggregates result of multiple oracles).
- [smart_oracle](https://github.com/DanielaIvanova/smart_oracle) - Oracles with Elixir.

###### Smart Contracts
- [aepp-sophia-examples](https://github.com/aeternity/aepp-sophia-examples) - A repository containing various Smart Contract examples.
- [contraect-showcase-maven](https://github.com/kryptokrauts/contraect-showcase-maven) - Demonstrates how to use the contraect-maven-plugin to generate Java classes for Smart Contract interactions.

###### State Channels
- [ae-channel-service](https://github.com/aeternity/ae-channel-service) - A reference client implementation written in Elixir.
    - [ae-backend-service](https://github.com/aeternity/ae-channel-service/blob/master/apps/ae_backend_service/README.md) - Backend service written specifically for the CoinToss demo to simulate a casino that acts as responder and orchestrates multiple channels.
- [coin-toss-game](https://github.com/aeternity/coin-toss-game) - The counterpart to the ae-backend-service which acts as initiator and opens channels with the simulated casino.

###### Other Examples
- [aepp-showcase-android](https://github.com/kryptokrauts/aepp-showcase-android) - Example native Android app using the Java SDK.

###### Code-Snippets
- [ae-snippets-node-js](https://github.com/kryptokrauts/ae-snippets-nodejs) - Node.js snippets to interact with Smart Contracts.

### Hackathons
- 21.04.2021 - 07.05.2021, [Akshwani Haeck](https://akshwanihaeck.devpost.com/) - Real world data, straight into the blocks!
- 10.11.2020 - 10.12.2020, [Human DeFi Haeck](https://humandefihaeck.devpost.com/) - Because DeFi can make life better for everyone.
    - https://blog.aeternity.com/the-human-defi-h%C3%A6ck-winners-announcement-ca1777f374e6
- 14.09.2019 - 15.09.2020, [æternity Universe One Hæckathon](https://aeternityuniverse.com/haeckathon)
    - Winners announcement: https://www.youtube.com/watch?v=tVCHP9L9xXA
    - https://github.com/aeternity/hackathon-prague
    - https://kryptokrauts.com/log/kryptokrauts-wins-aeternity-hackathon
    - https://hack.bg/blog/events/aeternity-universe-one/
- 27.11.2017 - 15.12.2017, [æpps Hackathon](https://blog.aeternity.com/aepps-hackathon-16e2d4f3e7d4)
    - https://blog.aeternity.com/announcing-the-top-3-hackathon-%C3%A6pps-a8e39b11764

## Decentralized Applications (æpps)

###### æternity projects
- [Governance æpp](https://governance.aeternity.com) - Voting for governance proposals with a delegated weighted polling mechanism.
    - https://github.com/aeternity/aepp-governance
- [Graffiti æpp](https://graffiti.aeternity.com)
    - https://github.com/aeternity/aepp-graffiti
- [Hybrid Voting](http://aeternity.com/aepp-hybrid-voting/) - Hybrid voting æpp that collected votes on Ethereum and æternity for the BRI vote.
    - https://github.com/aeternity/aepp-hybrid-voting
- [Superhero](https://superhero.com) - A user-centric, open source, decentralized - P2P social platform that elevates the impact of communities and user generated content with the help of blockchain technology.
    - Source Code:
        - https://github.com/aeternity/tipping-contract
        - https://github.com/aeternity/tipping-oracle-service
        - https://github.com/aeternity/tipping-community-backend
        - https://github.com/aeternity/superhero-ui
        - https://github.com/aeternity/superhero-button
    - Articles:
        - https://blog.aeternity.com/superhero-how-to-send-receive-superhero-tips-34971b18c919
        - https://blog.aeternity.com/wiki-how-superhero-voting-works-86eae25b6a3a
        - https://blog.aeternity.com/superhero-rises-its-time-to-fight-back-d11b4494bcc0
        - https://kryptokrauts.com/log/superhero-a-truly-decentralized-social-tipping-platform
- [Token Migration](https://migrate.aeternity.io) - This æpp helps you migrating old Ethereum based ERC-20 tokens.
    - https://github.com/aeternity/aepp-token-migration-holders
    - https://github.com/aeternity/aepp-token-migration-smart-contract
    - https://github.com/aeternity/aepp-token-migration-backend
        - Currently broken, will be migrated to Node.js
    - https://github.com/aeternity/aepp-token-migration

###### Other projects
- [AMPnet](https://ampnet.io) - Investment & tokenization platform with an integrated marketplace and a multinational legal entity.
    - https://www.youtube.com/watch?v=5FYvJ29aM48
- [Assetify](https://www.assetify.net) - Lending platform.
- [Cryptic Legends](https://www.crypticlegends.co/) - Decentralized game.
- [CryptoTask](https://app.cryptotask.org/) - Online platform for freelancers.
    - https://www.youtube.com/watch?v=R8552t2Tr0E
- [DRIFE](https://www.drife.io) - Decentralized ride-hailing platform which aims at
empowering both the driver and rider communities.
- [GamerHash](https://gamerhash.com) - Share computing power and earn.
    - https://medium.com/we-are-the-gamerhash/gamerhash-partners-up-with-%C3%A6ternity-72c36593595a
- [Homeport](https://homeport.network) - A global, user-centric ground station network.
- [Hypersign](https://hypersign.id) - Identity and access management solution.
    - https://www.youtube.com/watch?v=8Ush21_Mg9I
- [ReCheck](https://recheck.io/) - Objective and transparent rating of the energy and well-being performance of commercial real estate.
    - https://blog.aeternity.com/in-the-spotlight-recheck-daf4580f804
- [Say Network](https://www.say.network/) - Verifiable oracles.
- [SmartCredit](https://smartcredit.io) - A decentralized peer-to-peer global lending marketplace by connecting lenders and borrowers without intermediaries.
    - https://medium.com/smartcredit-io/aeternity-blockchain-and-smartcredit-io-and-defi-116e337d7856
- [Uruguay Can (Ucan)](https://ucan.uy) - A blockchain control and traceability system, from sowing to the final product, ensuring the quality of their processes and products.
- [Vereign](https://www.vereign.com) - Advanced protection technology designed to work with your existing infrastructure to add authenticity, security and trust to your inbox.
    - https://blog.aeternity.com/in-the-spotlight-vereign-69413d58f041
    - https://www.youtube.com/watch?v=SoNrLswGae0
- [WeiDex](https://github.com/weidex-team/weidex-ae) - Implementation of an exchange in Sophia.
- [WeTrue](https://wetrue.io) - Social æpp developed by the Chinese community.

###### Blog articles
- https://blog.aeternity.com/%C3%A6ternity-for-all-bbf11ab79073
- https://blog.aeternity.com/%C3%A6ternity-for-all-9c7cd1fab7a1

## Education

### Courses
- [Dacade](https://dacade.org/ae-dev-101/submissions) - An online learning platform that provides an introduction course to æternity and smart contract development.
- Sophia courses
    - [Basic course](https://drive.google.com/file/d/1NIhiVcByLmg9VcTcHqxcVo7oT112Bz2O/view)
    - [Intermediate course](https://drive.google.com/file/d/1k6vAWLLDePMaOX5-hD69JIKpDWqTuXf3/view)

### Documentation
- https://github.com/aeternity/tutorials - Collection of various tutorials
    - Some of those tutorials are currently outdated!

### Videos
- [æternity development](https://www.youtube.com/watch?v=POVc5pLthAI&list=PLZTjth8D1qBd47Qs3miHKtrHrxPzFpQ-3) - YouTube Playlist with educational content on æternity development.
- [æternity Developers and Researchers - Weekly updates](https://www.youtube.com/watch?v=df19MoKISVk&list=PLZTjth8D1qBfz8giWgAuMwBr88JCQNHp1) - YouTube Playlist with all updates that were publicly discussed in the past.
- [æternity Universe One - interviews](https://www.youtube.com/watch?v=U0hBNqtwwV0&list=PLZTjth8D1qBel9nv0EA4UOrUeV3o7Crf4) - YouTube Playlist containing all interviews of the æternity Universe One conference.
- [æternity Universe One - event presentations](https://www.youtube.com/playlist?list=PLZTjth8D1qBcd7GZmJ0Od5CTRei232hac) - YouTube Playlist containing all event presentations of the æternity Universe One conference.
- [æternity Webinars](https://www.youtube.com/watch?v=zNYa0V8dUiE&list=PLZTjth8D1qBe8H_79KlR3BVLkDOdqIJk1) - YouTube Playlist with webinars that were hosted in the past.
- [Community developer tutorials](https://www.youtube.com/playlist?list=PLZTjth8D1qBciVMK1xU56SSzTOZBSazot) - YouTube Playlist with videos created by the community.

## Exchanges

###### Withdrawal & Deposit
- [CoinW](https://www.coinw.com/) - Singapore cryptocurrency exchange.
- [Gate.io](https://www.gate.io) - Chinese assets trading platform.

###### Trading Only
- [AEX](https://www.aex88.com) - Seychelles cryptocurrency exchange.
- [CoinBene](https://www.coinbene.com) - Singapore cryptocurrency exchange.
- [DragonEx](https://dragonex.io) - Singapore cryptocurrency exchange.
- [HitBTC](https://hitbtc.com) - American cryptocurrency exchange.
- [HOTBIT](https://www.hotbit.io) - Chinese cryptocurrency exchange.
- [HuobiGlobal](https://www.huobi.com) - Chinese cryptocurrency exchange.
- [Jelly Swap](https://jelly.market) - Fast and secure way to swap coins.
- [MEXC Global](https://www.mexc.com) - Chinese assets trading platform.
- [OKEx](https://www.okex.com) - Maltese cryptocurrency exchange.
- [Tokok](https://www.tokok.com) -  British Virgin Islands cryptocurrency exchange.
- [ZB](https://www.zb.com/) - Chinese cryptocurrency exchange.
