class Pdi < Formula
  desc "Product Design Intelligence (PDI) — Principal Product Designer skills for AI agents"
  homepage "https://github.com/otherthngz/product-design-intelligence"
  url "https://github.com/otherthngz/product-design-intelligence/archive/refs/tags/v1.0.0.tar.gz"
  version "1.0.0"
  license "MIT"

  depends_on "python@3.11"

  def install
    libexec.install ".agents", "AGENTS.md", "adapters", "docs", "examples", "knowledge",
                    "scripts", "templates", "tests", "workflows"
    (bin/"pdi").write <<~EOS
      #!/bin/sh
      exec "#{Formula["python@3.11"].opt_bin}/python3" "#{libexec}/scripts/install_pdi.py" "$@"
    EOS
    (bin/"pdi-audit").write <<~EOS
      #!/bin/sh
      exec "#{Formula["python@3.11"].opt_bin}/python3" "#{libexec}/scripts/audit_artifact.py" "$@"
    EOS
  end

  test do
    system "#{bin}/pdi", "--help"
  end
end
