---
title: Portfolio - Kevin "Tyler" Cox
layout: home
---

<section class="portfolio-hero">
  <p class="hero-kicker">Senior software engineer · Charleston, SC · Open to remote roles</p>
  <h1>I build software for complex systems that cannot afford to be opaque.</h1>
  <p class="hero-lede">
    I am Kevin "Tyler" Cox, a software engineer with 11+ years of experience across
    Angular, backend integrations, platform tooling, observability, and delivery automation.
    I turn stateful systems into products that are testable, measurable, and practical to operate.
  </p>
  <div class="hero-actions">
    <a class="portfolio-button primary" href="#featured-work">Explore my work</a>
    <a class="portfolio-button" href="{{ '/resume/software-engineer.pdf' | relative_url }}">Download resume</a>
    <a class="portfolio-button quiet" href="mailto:{{ site.data.resume.email }}">Email me</a>
  </div>
</section>

<section class="impact-strip" aria-label="Career highlights">
  <div><strong>11+ years</strong><span>shipping production software</span></div>
  <div><strong>Angular at scale</strong><span>Signals, RxJS, NgRx</span></div>
  <div><strong>Full stack</strong><span>Java, .NET, Node.js, Firebase</span></div>
  <div><strong>Platform minded</strong><span>CI/CD, Kubernetes, observability</span></div>
</section>

<section id="featured-work" class="portfolio-section">
  <div class="section-heading">
    <p class="section-kicker">Selected work</p>
    <h2>Systems built from the difficult parts outward</h2>
  </div>

  <div class="featured-grid">
    <article class="feature-card feature-card-lead">
      <div>
        <span class="status-badge">Current · Framework & platform</span>
        <h3>Reverse-engineered game server modding framework</h3>
        <p>
          A server-side modding and operations stack created by reverse-engineering a
          commercial multiplayer game's proprietary Windows dedicated server.
        </p>
      </div>
      <ul class="compact-list">
        <li>UE4SS/Lua runtime and authenticated Node.js bridge</li>
        <li>Native C++ hooks and frame-time telemetry</li>
        <li>Angular/Electron operator console, CLI, repair, and rollback</li>
      </ul>
      <a class="card-link" href="{{ '/posts/reverse-engineered-game-server-modding-framework/' | relative_url }}">Read the engineering case study →</a>
    </article>

    <article class="feature-card">
      <div>
        <span class="status-badge">Current · Full stack</span>
        <h3>CityRPG</h3>
        <p>
          A server-authoritative multiplayer roleplay platform spanning TypeScript,
          Angular 20, Firebase, Rust world tooling, and a .NET 8 Windows companion.
        </p>
      </div>
      <ul class="compact-list">
        <li>Transactional economy and persistent player systems</li>
        <li>340+ automated test files and emulator-backed rules tests</li>
        <li>Guarded rollout paths for high-risk integrations</li>
      </ul>
      <a class="card-link" href="{{ '/posts/cityrpg-overview/' | relative_url }}">Explore the platform →</a>
    </article>

    <article class="feature-card">
      <div>
        <span class="status-badge">Professional · Enterprise</span>
        <h3>Logistics applications & platform engineering</h3>
        <p>
          More than a decade building Angular applications, service integrations,
          identity controls, delivery automation, and observability for logistics operations.
        </p>
      </div>
      <ul class="compact-list">
        <li>Angular, TypeScript, Java/Spring Boot, and C#/.NET</li>
        <li>Grafana, Prometheus, Loki, Tempo, SLOs, and alerting</li>
        <li>GitHub Actions, GitLab Runners, Ansible, Kubernetes, and GCP</li>
      </ul>
      <a class="card-link" href="{{ '/posts/workboard-app-overview/' | relative_url }}">See an application case study →</a>
    </article>
  </div>
</section>

<section class="portfolio-section capability-section">
  <div class="section-heading">
    <p class="section-kicker">Core capabilities</p>
    <h2>From user interface to operating model</h2>
    <p>I am most useful where product engineering, platform concerns, and system behavior meet.</p>
  </div>
  <div class="skill-groups">
    {% for group in site.data.resume.skills %}
      <div class="skill-group">
        <h3>{{ group.title }}</h3>
        <div class="skill-cloud">
          {% for skill in group.skills %}<span>{{ skill }}</span>{% endfor %}
        </div>
      </div>
    {% endfor %}
  </div>
</section>

<section class="portfolio-section career-section">
  <div class="career-card">
    <div>
      <p class="section-kicker">What I am looking for</p>
      <h2>Senior or Software Engineer III+ work with real system ownership.</h2>
    </div>
    <p>
      I am targeting remote U.S. roles in full-stack engineering, frontend platform,
      developer infrastructure, or observability—especially teams solving operationally
      meaningful problems with TypeScript, Angular, Java, .NET, Node.js, or cloud-native tooling.
    </p>
    <div class="hero-actions">
      <a class="portfolio-button primary" href="mailto:{{ site.data.resume.email }}">Start a conversation</a>
      <a class="portfolio-button" href="{{ site.data.resume.socialMedia[1].link }}">LinkedIn</a>
      <a class="portfolio-button quiet" href="{{ site.data.resume.socialMedia[0].link }}">GitHub</a>
    </div>
  </div>
</section>
